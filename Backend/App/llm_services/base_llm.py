from abc import ABC, abstractmethod


class BaseLLM(ABC):


    @abstractmethod
    def generate_tests(
        self,
        requirement: str
    ):
        pass