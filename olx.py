import requests
from bs4 import BeautifulSoup

from schemas import Offer


class Olx:
    def __init__(self, urls: list[str]) -> None:
        self.urls = urls
        self.offers = []

    def start(self) -> None:
        offers = self.get_offers()
        new_offers = [offer for offer in offers if self.is_new_offer(offer)]
        self.offers.extend(new_offers)

    def run(self) -> list[Offer]:
        offers = self.get_offers()
        new_offers = [offer for offer in offers if self.is_new_offer(offer)]
        self.offers.extend(new_offers)
        return new_offers

    def get_offers(self) -> list[Offer]:
        offers = []

        for url in self.urls:
            offers_from_url = self.get_offers_from_url(url)
            offers.extend(offers_from_url)

        return offers

    def get_offers_from_url(self, url: str) -> list[Offer]:
        all_offers = []
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        soup_offers = soup.find_all("div", {"data-cy": "l-card"})
        for soup_offer in soup_offers:
            title = soup_offer.find("h6").text
            promoted = soup_offer.find("div", {"data-testid": "adCard-featured"}) is not None
            price = soup_offer.find("p", {"data-testid": "ad-price"}).text
            link = soup_offer.find("a")["href"]
            is_today = (
                "dzisiaj" in soup_offer.find("p", {"data-testid": "location-date"}).text.lower()
            )
            offer = Offer(title, promoted, price, link, is_today)
            all_offers.append(offer)

        return all_offers

    def is_new_offer(self, offer: Offer) -> bool:
        if offer.promoted:
            return False

        if not offer.is_today:
            return False

        for saved_offer in self.offers:
            if saved_offer.link == offer.link:
                return False

        return True
