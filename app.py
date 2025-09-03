from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import uuid
from datetime import datetime
from classify_food import FoodClassifier
from nutrition_database import NutritionDatabase

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('models', exist_ok=True)

# Initialize classifier and database
food_classifier = FoodClassifier()
nutrition_db = NutritionDatabase()


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def cleanup_old_uploads():
    """Remove old uploaded files (older than 1 hour)"""
    try:
        current_time = datetime.now().timestamp()
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                file_age = current_time - os.path.getmtime(filepath)
                if file_age > 3600:  # 1 hour
                    os.remove(filepath)
    except Exception as e:
        print(f"Error cleaning up files: {e}")


@app.route('/')
def index():
    """Homepage with landing page"""
    cleanup_old_uploads()
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and classification"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        # Generate unique filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f"{uuid.uuid4()}.{ext}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Save file
        file.save(filepath)

        # Classify the image
        result = food_classifier.classify(filepath)

        if result['success']:
            # Store in session for results page
            session['last_result'] = {
                'image_path': f'uploads/{filename}',
                'food': result['food'],
                'confidence': result['confidence'],
                'all_predictions': result.get('all_predictions', {})
            }

            # Add to scan history
            if 'scan_history' not in session:
                session['scan_history'] = []

            session['scan_history'].append({
                'food': result['food'],
                'confidence': result['confidence'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'image_path': f'uploads/{filename}'
            })

            # Keep only last 10 scans
            session['scan_history'] = session['scan_history'][-10:]

            return jsonify({
                'success': True,
                'redirect': url_for('results')
            })
        else:
            # Clean up uploaded file if classification failed
            os.remove(filepath)
            return jsonify({
                'error': f"Classification failed: {result.get('error', 'Unknown error')}"
            }), 500

    return jsonify({'error': 'Invalid file type'}), 400


@app.route('/results')
def results():
    """Display classification results and nutritional information"""
    if 'last_result' not in session:
        return redirect(url_for('index'))

    result = session['last_result']

    # Get nutritional information
    nutrition = nutrition_db.get_nutrition(result['food'], 100)

    return render_template('results.html',
                           result=result,
                           nutrition=nutrition)


@app.route('/get_nutrition/<food_name>/<int:serving_size>')
def get_nutrition(food_name, serving_size):
    """API endpoint to get nutritional information for specific serving size"""
    nutrition = nutrition_db.get_nutrition(food_name, serving_size)

    if nutrition:
        return jsonify(nutrition)
    else:
        return jsonify({'error': 'Food not found'}), 404


@app.route('/compare')
def compare():
    """Food comparison page"""
    scan_history = session.get('scan_history', [])
    all_foods = nutrition_db.get_all_foods()
    return render_template('compare.html',
                           scan_history=scan_history,
                           all_foods=all_foods)


@app.route('/compare_foods', methods=['POST'])
def compare_foods():
    """API endpoint to compare two foods"""
    data = request.json
    food1 = data.get('food1')
    food2 = data.get('food2')
    serving_size = data.get('serving_size', 100)

    comparison = nutrition_db.compare_foods(food1, food2, serving_size)

    if comparison:
        return jsonify(comparison)
    else:
        return jsonify({'error': 'Could not compare foods'}), 400


@app.route('/clear_history')
def clear_history():
    """Clear scan history"""
    session.pop('scan_history', None)
    return redirect(url_for('compare'))


@app.route('/about')
def about():
    """About page"""
    return render_template('index.html', scroll_to='about')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
