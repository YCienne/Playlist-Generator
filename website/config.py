import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
    
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
    
    ROBOFLOW_MODEL_ID = os.getenv("ROBOFLOW_MODEL_ID")
    
    UPLOAD_FOLDER = "uploads"
    
