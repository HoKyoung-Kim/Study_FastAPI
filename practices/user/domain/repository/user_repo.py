from abc import ABCMeta, abstractmethod
from user.domain.user import User

class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User):
        raise NotImplementedError
    
    @abstractmethod
    def find_by_email(self, email: str) -> User:
        '''
        이메일로 User를 찾고, 없을 시 422 에러를 발생시킨다.
        '''
        raise NotImplementedError
