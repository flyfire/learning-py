from abc import abstractmethod


class BaseWidget:
    @abstractmethod
    def process(self):
        pass
