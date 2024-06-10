
from telegram import Bot
from telegram.error import TelegramError
import requests

class TelegramMsg:
    def __init__(self, bot_token, chat_id):
        self.bot_token = "<TOKEN ADDRESS OF YOUR TELEGRAM CHATBOT>"
        self.chat_id = "<ID NUMBER OF YOUR TELEGRAM ACCOUNT>"
        self.bot = Bot(token=bot_token)

    async def send_message_async(self, text):
        try:
            await self.bot.send_message(chat_id=self.chat_id, text=text)
            print("Message Sent.")
        except TelegramError as e:
            print(f"Message Send Error: {e}")

    @staticmethod
    def send_telegram_message(bot_token, chat_id, message):
        api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(api_url, json=payload)
        return response.json()