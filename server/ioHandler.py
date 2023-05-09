from abc import ABC, abstractmethod

class IOHandler(ABC):
    @abstractmethod
    def  accept_client_connection(self):
        pass

    @abstractmethod
    def handle_client(self):
        pass

    @abstractmethod
    def start_server(self):
        pass
