from unittest import TestCase, main
import os

class Tests(TestCase):
    def setUp(self):
        from dotenv import load_dotenv
        load_dotenv()
        
    def test_bot_token(self):
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.assertIsInstance(bot_token, str)

    def test_chat_id(self):
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.assertIsInstance(chat_id, str)

    def test_send_message(self):
        from src.telegram import TelegramBot
        bot = TelegramBot()
        bot.send_message('Hello World!')

if __name__ == '__main__':
    main()