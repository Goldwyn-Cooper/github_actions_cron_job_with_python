if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    import warnings
    warnings.filterwarnings('ignore')
    import requests
    from src.telegram import TelegramBot
    try:
        bot = TelegramBot()
        bot.send_message('Hello World!')
    except requests.exceptions.HTTPError as e:
        print(e.response.status_code, e.response.reason)
    except Exception as e:
        print(type(e))
        print(e)
