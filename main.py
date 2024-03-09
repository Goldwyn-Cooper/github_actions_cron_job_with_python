if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    from src.telegram import TelegramBot
    bot = TelegramBot()
    bot.send_message('Hello World!')