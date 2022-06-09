import time

from settings import get_settings, Settings
from olx import Olx
from telegram import TelegramClient

settings: Settings = get_settings()


def main():
    telegram = TelegramClient(settings.telegram_token, settings.telegram_chat_id)
    olx = Olx(settings.olx_urls)
    olx.start()

    time.sleep(settings.start_sleep_time)

    while True:
        try:
            new_offers = olx.run()
        except:
            print("Getting new offers failed")
            time.sleep(settings.sleep_time)
            continue

        for offer in new_offers:
            text = f"""
            {offer.title} - {offer.price}

            {offer.link}
            """
            try:
                telegram.send(text)
            except:
                print("Sending offer to telegram failed")

        time.sleep(settings.sleep_time)


if __name__ == "__main__":
    main()
