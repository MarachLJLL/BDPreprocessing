from abc import ABC, abstractmethod

class JDParser(ABC):
    @abstractmethod
    def parse(jd):
        pass