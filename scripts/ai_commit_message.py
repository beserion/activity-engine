import os
import requests
import json

API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set!")

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

try:
    res = requests.post(URL, json=payload, timeout=10)
    res.raise_for_status()
    data = res.json()

    # 🛡️ API yanıt kontrolü
    msg = "chore: küçük değişiklik"  # fallback mesaj
    if "candidates" in data and len(data["candidates"]) > 0:
        msg = data["candidates"][0]["content"]["parts"][0].get("text", msg).strip()

except (requests.RequestException, KeyError, IndexError, json.JSONDecodeError) as e:
    print(f"⚠️ Gemini API hatası: {e}")
    msg = "chore: küçük değişiklik"  # fallback mesaj

# commit mesajını yaz
with open("commit_msg.txt", "w", encoding="utf-8") as f:
    f.write(msg)

print("Commit message:", msg)
