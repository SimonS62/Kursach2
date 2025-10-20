from abc import ABC, abstractmethod

class AbstractFile(ABC):
    @abstractmethod
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, data):
        pass
