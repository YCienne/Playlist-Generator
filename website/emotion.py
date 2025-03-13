import os
from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key= os.getenv("ROBOFLOW_API_KEY")  
)

MODEL_ID = os.getenv("ROBOFLOW_MODEL_ID")

def detect_emotion_from_image(image_path):
    try:
        result = CLIENT.infer(image_path, model_id=MODEL_ID)

        if "predictions" in result and len(result["predictions"]) > 0:
            detected_emotion = result["predictions"][0]["class"]
            print(f"Detected Emotion: {detected_emotion}")
            return detected_emotion
        else:
            print("No face detected!")
            return "neutral"

    except Exception as e:
        print(f"Roboflow API Error: {e}")
        return "neutral"
