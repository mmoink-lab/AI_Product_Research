from abc import ABC, abstractmethod


class BaseScraper(ABC):

    @abstractmethod
    def search(self, keyword):
        pass

    @abstractmethod
    def close(self):
        pass