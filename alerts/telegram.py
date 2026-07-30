"""
Telegram Alert Sender
"""

import requests


class TelegramAlert:

    def __init__(self, bot_token, chat_id):

        self.bot_token = bot_token
        self.chat_id = chat_id

    def send(self, event):

        message = (
            "🚨 FALL DETECTED\n\n"
            f"Track ID : {event['track_id']}\n"
            f"Confidence : {event['confidence']:.1f}%\n"
            f"State : {event['state']}"
        )

        url = (
            f"https://api.telegram.org/bot{self.bot_token}"
            "/sendMessage"
        )

        payload = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:
            requests.post(url, data=payload, timeout=10)
            print("[Telegram] Alert sent.")

        except Exception as e:
            print(f"[Telegram] Error: {e}")