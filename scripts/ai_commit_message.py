import os
import requests
import json

API_KEY = os.environ["GEMINI_API_KEY"]
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

prompt = """
Generate a short, natural Git commit message.

Rules:
- Max 8 words
- No emojis
- Casual but professional
- Looks human, not robotic

Examples:
docs: small clarification
chore: minor cleanup
refactor: tiny improvement
"""

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

res = requests.post(URL, json=payload)
data = res.json()

msg = data["candidates"][0]["content"]["parts"][0]["text"].strip()

with open("commit_msg.txt", "w", encoding="utf-8") as f:
    f.write(msg)

print("Commit message:", msg)
