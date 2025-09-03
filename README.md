NutriVision – AI Food Recognition & Nutrition Analysis

NutriVision is a Flask-based web application that uses YOLOv8 for food recognition and provides detailed nutritional analysis.
It allows users to upload food images, analyze nutritional breakdowns, and compare foods side by side with allergen and dietary insights.

Features

AI-Powered Food Recognition
Detects food items from uploaded images using a trained YOLOv8 model.

Nutritional Breakdown
Displays calories, protein, carbs, fat, fiber, sugar, sodium, and vitamin content per serving.

Food Comparison
Compare two foods side by side with health indicators (better, worse, neutral).

Dietary & Allergen Insights
Provides allergen warnings, dietary tags (vegan, gluten-free, etc.), and health benefits.

Scan History
Keeps track of recent scans for quick re-analysis and comparison.



PROJECT STRUCTURE
NutriVision/
│── app.py                  # Flask application entry point
│── classify_food.py        # YOLOv8-based food classifier
│── nutrition_database.py   # Nutrition database with detailed food info
│── templates/
│   ├── index.html          # Landing page & upload interface
│   ├── results.html        # Food analysis results
│   ├── compare.html        # Food comparison page
│── static/
│   ├── uploads/            # Uploaded food images
│   └── css/js/assets       # Static assets
│── models/
│   └── best.pt             # Trained YOLOv8 classification model (not included)



API Endpoints

POST /upload → Upload and classify food image

GET /results → Display results for last upload

GET /get_nutrition/<food>/<serving_size> → JSON nutrition data

GET /compare → Food comparison interface

POST /compare_foods → Compare two foods (returns JSON)

GET /clear_history → Clears stored scan history

Supported Foods

The model and nutrition database currently support:

Sushi

Bibimbap

Apple Pie

Tiramisu

Cannoli

Edamame

Falafel

French Toast

Ice Cream

Ramen

(Extendable via nutrition_database.py and retraining the model.)





