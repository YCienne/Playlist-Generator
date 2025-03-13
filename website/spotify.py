import requests
import os

def get_spotify_playlists(emotion):
    
    mood_mapping = {
        "happy": "happy upbeat pop hits",
        "sad": "chill sad acoustic songs",
        "angry": "high-energy rock and metal",
        "surprise": "fun party anthems",
        "neutral": "relaxing instrumental music",
        "fear": "calm soothing music",
        "disgust": "feel-good classic hits", 
    }
    
    query = mood_mapping.get(emotion.lower(), "mood booster music")  
    print(f"Searching for Spotify playlists: {query}")

    try:
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

        auth_response = requests.post("https://accounts.spotify.com/api/token", {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        })
        auth_response_data = auth_response.json()
        access_token = auth_response_data.get("access_token")

        if not access_token:
            print("Error getting Spotify token")
            return []

        headers = {"Authorization": f"Bearer {access_token}"}
        url = f"https://api.spotify.com/v1/search?q={query}&type=playlist&limit=5"
        response = requests.get(url, headers=headers)
        data = response.json()

        playlists = data.get("playlists", {}).get("items", [])
        playlist_list = []

        for playlist in playlists:
            if playlist:
                playlist_info = {
                    "name": playlist.get("name", "Unknown Playlist"),
                    "url": playlist["external_urls"]["spotify"],
                    "image": playlist["images"][0]["url"] if playlist.get("images") and playlist["images"] else None
                }
                playlist_list.append(playlist_info)

        if playlist_list:
            print(f"Playlists Found: {playlist_list}")
            return playlist_list

        print("No valid playlists found!")
        return []

    except Exception as e:
        print(f"Spotify API Error: {e}")
        return []
