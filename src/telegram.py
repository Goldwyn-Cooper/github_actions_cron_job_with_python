import os
import warnings
warnings.filterwarnings('ignore')
import requests

class TelegramBot:
    def __init__(self):
        self.token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not self.token:
            raise ValueError('TELEGRAM_BOT_TOKEN is not set')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        if not self.chat_id:
            raise ValueError('TELEGRAM_CHAT_ID is not set')
        self.url = f'https://api.telegram.org/bot{self.token}/'

    def send_message(self, text):
        params = dict(chat_id=self.chat_id, text=text)
        response = requests.post(self.url + 'sendMessage', params)
        response.raise_for_status()
    
    def get_chat_id(self):
        response = requests.get(self.url + 'getUpdates')
        response.raise_for_status()
        data = response.json()
        chat_id = data['result'][-1]['message']['chat']['id']
        return chat_id

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    bot = TelegramBot()
    print(bot.get_chat_id())
    bot.send_message(bot.chat_id, 'Hello World!')