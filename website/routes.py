from flask import Blueprint, render_template, request, jsonify
import os
from website.emotion import detect_emotion_from_image
from website.llm import generate_music_mood
from website.spotify import get_spotify_playlists
import json

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/detect-emotion", methods=["POST"])
def detect_emotion():
    try:
        image = request.files["image"]
        image_path = os.path.join("uploads", image.filename)
        image.save(image_path)
        detected_emotion = detect_emotion_from_image(image_path)

        music_mood = generate_music_mood(detected_emotion)
        playlists = get_spotify_playlists(detected_emotion)

        print(f"Emotion: {detected_emotion}")
        print(f"Music Mood: {music_mood}")
        print(f"Playlists JSON: {json.dumps(playlists, indent=2)}") 

        return jsonify({
            "emotion": detected_emotion,
            "music_mood": music_mood,
            "playlists": playlists  
        })

    except Exception as e:
        print(f"Error in /detect-emotion: {e}")
        return jsonify({"error": str(e)})

