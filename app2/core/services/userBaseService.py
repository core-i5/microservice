from abc import ABC, abstractmethod


class UserBaseService(ABC):

    @abstractmethod
    def get_all(self):
        """ 
        Abstract method to get all users.
        """
        pass