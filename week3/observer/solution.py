from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscribe)
    
    def unsubscribe(self):
        self.__subscribers.remove(subscriber)

    def notify(self, achiev):
        for subscribe in self.__subscribers:
            subscribe.update(achiev)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achiev):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievments = set()

    def update(self, achiev):
        self.achievments.add(achiev['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achiev):
        if achiev not in self.achievements:
            self.achievements.append(achiev)
