class Drink:
    _CUPS = ('레귤러', '점보')   # 레귤러
    _ICES = ('0%', '50%', '100%', '150%')   # 100%
    _SUGARS = ('0%', '50%', '100%', '150%') # 100%

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0    # 레귤러
        self.ice = 2    # 100%
        self.sugar = 2  # 100%

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):   #컵 종류 보여주기
            print(f'{index + 1}: {cup}')
        cup = input('컵사이즈를 선택하세요: ')    #컵 선택하자
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup)
            self.cup = cup - 1  #컵 self에 넣자

        if self.cup == 1:
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):  # 컵 종류 보여주기
            print(f'{index + 1}: {ice}')
        # 컵 선택하자
        ice = input('얼음량을 선택하세요: ')#선택하자
        #if ice = '':
        #   self.ice = 2
        #else:
        #   self.ice = int(ice) - 1
        self.ice = 2 if ice == '' else int(ice) - 1
    def set_sugar(self):
        pass

    def __str__(self):
        return f'이름 : {self.name}\t가격 : {self.price}\t컵사이즈 : {Drink._CUPS[self.cup]}\t얼음량 : {Drink._ICES[self.ice]}\t당도 : {Drink._SUGARS[self.sugar]}'

class Coffee(Drink):
    pass

class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')
    def __init__(self, name, price):
        super().__init__(self. name, price)
        self.pearl = 0       #'타피오카'
    def __str__(self):
        pass

사랑이 = Drink('카페모카', 2500)
사랑이.order()
print(사랑이)