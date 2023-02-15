from abc import ABC, abstractmethod


class UserBaseService(ABC):

    @abstractmethod
    def get_all(self):
        """ 
        Abstract method to get all users.
        """
        pass

    @abstractmethod
    def create(self):
        """
        Abstract method to create user.
        """
        pass

    @abstractmethod
    def delete(self):
        """
        Abstract method for deletion of user.
        """
        pass