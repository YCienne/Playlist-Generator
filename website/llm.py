import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_music_mood(emotion):
    try:
        prompt = f"""
        Based on the emotion "{emotion}", suggest the ideal type of music that matches this mood.
        Explain why this music genre is suitable for this emotion in a fun and engaging way.
        Keep the explanation concise and friendly (2-3 sentences).
        """
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a music recommendation expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Music is a great way to enhance your mood!"
