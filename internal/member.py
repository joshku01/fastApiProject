import abc
from abc import ABC, abstractmethod


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def info(self):
        print(f'{self.firstname}: {self.lastname}')


class Member(Person):
    def __init__(self, first, last, member_id, fee):
        # 關鍵字 使用super()繼承
        super().__init__(first, last)
        self.member_id = member_id
        self.fee = fee

    def info(self):
        super().info()
        print(f'會員編號:{self.member_id},金額:{self.fee}')

    def get_discount(self):
        self.fee = self.fee - 0.1 * self.fee
        print(f'折扣後{self.fee}元')


class GoldMember(Member):
    def get_discount(self):
        self.fee = self.fee - 0.3 * self.fee
        print(f'折扣後{self.fee}元')

    def info(self):
        super().info()
        print("您是金卡會員")


class SilverMember(Member):
    point = 100

    def get_discount(self):
        self.fee = self.fee - 0.2 * self.fee
        print(f'折扣後{self.fee}元')

    def info(self):
        super().info()
        print("您是銀卡會員")

    # 用self.__cloass__屬性來改變point類別屬性
    def change_status(self):
        self.__class__.point = 200

    @staticmethod
    def sopping_cart(item, percent):
        return item / percent


class NormalMember(Member):
    def info(self):
        super().info()
        print("您是我們的會員")


class Login(ABC):
    # 抽象類登入方法
    @abstractmethod
    def login(self):
        pass


# 繼承抽象類別Login,並且實作login() method
class FacebookLogin(Login):
    def login(self):
        print('facebook login method')


class GoogleLogin(Login):
    def login(self):
        print('Google login method')


class LineLogin(Login):
    def login(self):
        print('Line login method')
