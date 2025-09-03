from ultralytics import YOLO
from PIL import Image
import os


class FoodClassifier:
    def __init__(self, model_path='models/best.pt'):
        """
        Initialize the food classifier with YOLOv8n-cls model

        Args:
            model_path: Path to the trained model
        """
        self.model_path = model_path
        self.model = None
        self.class_names = [
            'sushi', 'bibimbap', 'apple_pie', 'tiramisu',
            'cannoli', 'edamame', 'falafel', 'french_toast',
            'ice_cream', 'ramen'
        ]
        self.load_model()

    def load_model(self):
        """Load the YOLOv8n-cls model"""
        try:
            if os.path.exists(self.model_path):
                self.model = YOLO(self.model_path)
                print(f"Model loaded successfully from {self.model_path}")
            else:
                print(f"Warning: Model file not found at {self.model_path}")
                print("Please ensure best.pt is placed in the models/ directory")
                # For testing without model, we'll create a dummy predictor
                self.model = None
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def preprocess_image(self, image_path):
        """
        Preprocess image for classification

        Args:
            image_path: Path to the image file

        Returns:
            Preprocessed image
        """
        try:
            # Open and convert image to RGB
            image = Image.open(image_path).convert('RGB')

            # Resize to model input size (usually 224x224 for classification)
            image = image.resize((224, 224))

            return image
        except Exception as e:
            print(f"Error preprocessing image: {e}")
            return None

    def classify(self, image_path):
        """
        Classify food in the image.

        Args:
            image_path: Path to the image file.

        Returns:
            Dictionary with classification results.
        """
        try:
            # Check if model is loaded
            if self.model is None:
                raise RuntimeError(
                    "Model not loaded. Please ensure 'best.pt' is in the 'models/' directory.")

            # Preprocess image
            image = self.preprocess_image(image_path)
            if image is None:
                raise ValueError("Failed to preprocess image.")

            # Run inference
            results = self.model(image)

            # Get predictions
            if results and len(results) > 0:
                result = results[0]

                # Get top prediction
                probs = result.probs
                top_class_idx = probs.top1
                top_confidence = float(probs.top1conf)

                # Get class name
                if hasattr(result, 'names'):
                    food_name = result.names[top_class_idx]
                else:
                    # Fallback to our predefined class names
                    food_name = self.class_names[top_class_idx] if top_class_idx < len(
                        self.class_names) else 'unknown'

                # Get all predictions with confidence scores
                all_predictions = {}
                if hasattr(probs, 'data'):
                    for idx, conf in enumerate(probs.data.tolist()):
                        if idx < len(self.class_names):
                            all_predictions[self.class_names[idx]] = round(
                                conf, 4)

                return {
                    'success': True,
                    'food': food_name,
                    'confidence': round(top_confidence, 4),
                    'all_predictions': all_predictions
                }
            else:
                raise RuntimeError("No predictions from model.")

        except Exception as e:
            print(f"Error during classification: {e}")
            return {
                'success': False,
                'error': str(e)
            }

    def get_top_predictions(self, image_path, top_k=3):
        """
        Get top-k predictions for the image

        Args:
            image_path: Path to the image file
            top_k: Number of top predictions to return

        Returns:
            List of tuples (food_name, confidence)
        """
        result = self.classify(image_path)

        if not result['success']:
            return []

        all_preds = result.get('all_predictions', {})
        sorted_preds = sorted(
            all_preds.items(), key=lambda x: x[1], reverse=True)

        return sorted_preds[:top_k]
