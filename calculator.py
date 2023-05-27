from currency_converter import CurrencyConverter
c = CurrencyConverter()

class Calculator:
    def __init__(self, first, second):
        self.set_data(first, second)
        self.country = ['USD', 'JPY', 'EUR', 'GBP', 'CAD', 'CHF', 'HKD', 'CNY', 'IDR', 'NOK', 'TRY', 'RUB']

    def set_data(self, first, second):
        if type(first) == int or type(first) == float:
            self.first = first
        if type(second) == int or type(second) == float:
            self.second = second

    def log_write(self, symbol, ans):
        with open("calculator_log.txt", "a", encoding="utf8") as log:
            log.write(f"{self.first} {symbol} {self.second} = {ans}\n")
    
    def add(self): #더하기
        result = self.first + self.second
        self.log_write("+", result)
        return result
    
    def sub(self): #빼기
        result = self.first - self.second
        self.log_write("-", result)
        return result
    
    def mul(self): #곱하기
        result = self.first * self.second
        self.log_write("*", result)
        return result
    
    def div(self): #나누기
        if self.second == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        result = self.first / self.second
        self.log_write("÷", result)
        return result
    
    def quo(self): #몫
        if self.second == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        self.log_write("//", result)
        result = self.first // self.second
        return result

    def rem(self): #나머지
        if self.second == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        self.log_write("mod", result)
        result = self.first % self.second
        return result
    
    def pow(self): #제곱
        result = self.first ** self.second
        self.log_write("^", result)
        return result
    
    def per(self): #백분율
        if self.second == 0:
            print("0으로 나눌 수 없습니다.")
            return None
        result = self.div() * 100
        self.log_write(":", str(result)+"%")
        return result
    
    def bit_and(self):
        result = self.first & self.second
        self.log_write("&", result)
        return result
    
    def bit_or(self):
        result = self.first | self.second
        self.log_write("|", result)
        return result
    
    def bit_xor(self):
        result = self.first ^ self.second
        self.log_write("^", result)
        return result
    
    def shift_left(self):
        result = self.first << self.second
        self.log_write("<<", result)
        return result

    def shift_right(self):
        result = self.first >> self.second
        self.log_write(">>", result)
        return result
    
    def er(self):
        if self.second >= len(self.country):
            print("숫자가 잘못 입력 되었습니다.")
            return
        result = c.convert(self.first, 'KRW', self.country[self.second])
        with open("calculator_log.txt", "a", encoding="utf8") as log:
            log.write(f"{self.first}KRW = {result:.2f}{self.country[self.second]}\n")
        return result
    
cal = Calculator(1000, 0)
cal.er()
cal.set_data(2,3)
cal.sub()
cal.set_data(5,2)
cal.pow()