import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

WELCOME_MESSAGE = """Welcome to CQpay!

Step 1: Log in to your account.
Step 2: Follow the instructions provided by support.
Step 3: Contact official support if you need assistance.
"""

@app.route("/", methods=["GET"])
def home():
    return "CQpay Telegram Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}

    message = data.get("message", {})
    chat = message.get("chat", {})
    text = message.get("text", "")

    if chat.get("id") and text == "/start":
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        requests.post(
            url,
            json={
                "chat_id": chat["id"],
                "text": WELCOME_MESSAGE
            },
            timeout=10
        )

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
