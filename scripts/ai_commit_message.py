import os
import requests
import json

# Fallback mesaj
msg = "chore: küçük değişiklik"

API_KEY = os.environ.get("GEMINI_API_KEY")
if API_KEY:
    URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": """
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
""" }]}
        ]
    }

    try:
        res = requests.post(URL, json=payload, timeout=10)
        res.raise_for_status()
        data = res.json()
        if "candidates" in data and len(data["candidates"]) > 0:
            msg = data["candidates"][0]["content"]["parts"][0].get("text", msg).strip()
    except Exception as e:
        print(f"⚠️ Gemini API hatası: {e}")
else:
    print("⚠️ GEMINI_API_KEY yok, fallback mesaj kullanılıyor")

# Her koşulda commit_msg.txt yaz
with open("../commit_msg.txt", "w", encoding="utf-8") as f:
    f.write(msg)

print("Commit message:", msg)
