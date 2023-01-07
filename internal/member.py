from abc import ABC, abstractmethod


class Person:
    def __init__(self, first, last, nickname):
        self.firstname = first
        self.lastname = last
        self.__nickname = nickname  # 前面使用__作為私有屬性

    def info(self):
        print(f'{self.firstname}: {self.lastname}')

    def __type(self, nickname):  # 使用__作為私有方法(private method)
        self.__nickname = nickname


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
    # 抽象類登入方法,抽象方法需要由繼承方式來實做
    @abstractmethod
    def login(self):
        pass


# 繼承抽象類別Login,並且實作login() method ,多型方法
class FacebookLogin(Login):
    def login(self):
        print('facebook login method')


class GoogleLogin(Login):
    def login(self):
        print('Google login method')


class LineLogin(Login):
    def login(self):
        print('Line login method')


class TwitterLogin(Login):
    level = 2  # 類別屬性

    @classmethod  # 類別方法使用@clossmethod 裝飾詞,由於參數為cls指向Class,僅能改變Class Method的狀態,無法改變物件狀態
    def login(cls):
        print(f"Twitter login member level is {cls.level}")

    @staticmethod  # 靜態方法,無法改變Class,Object狀態
    def accelerate():
        print('Accelerate is {0} {1}.'.format('statis', 'method'))  # 格式畫輸出方法,可以指定括號裡面順序
