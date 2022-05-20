from abc import ABC, abstractmethod
 
class Sendler(ABC):
    
    @abstractmethod
    def send_message(self, data):
        pass