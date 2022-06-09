import requests


class TelegramClient:
    def __init__(self, token: str, chat_id: str) -> None:
        self.token: str = token
        self.chat_id: str = chat_id
        self.url: str = "https://api.telegram.org"

    def send(self, text: str) -> None:
        base_url = f"{self.url}/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={text}"
        response = requests.get(base_url)
        print(response)
