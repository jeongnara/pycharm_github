class Celebrity:
    def __init__(self, name):
        # 이름
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)      #Celebrity 클래스(부모클래스)의 생성자 호출

    def set_drama(self, drama):
        self.drame = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drame}'

class Singer(Celebrity):
    def __init__(self, name, song):
        super().__init__(name)    #self.name = name
        self.song = song

    def __str__(self):
        return super().__str__() + f'\t노래: {self.song}'



IU = Celebrity('아이유')    #new Celebrity() in java
# IU.set_name('이지은')
IU.set_entertainment('이담')
print(IU.name, IU.entertainment)
print(IU)   #클래스의 __str__() 호출됨

백현 = Celebrity('변백현')    #new Celebrity() in java
# 백현.set_name('변백현')
백현.set_entertainment('SM')
print(백현)

이광수 = Talent('이광수')
이광수.set_entertainment('킹콩')
이광수.set_drama('라이브')
print(이광수)

현진 = Singer('현진', '神메뉴')
현진.set_entertainment('JYP')
print(현진)
필릭스 = Singer('필릭스', 'Back Door')
필릭스.set_entertainment('JYP')
print(필릭스)

스트레이키즈 = []
스트레이키즈.append(현진)
스트레이키즈.append(필릭스)
print(스트레이키즈)
for i in 스트레이키즈:
    print(i)
# for i in range(len(스트레이키즈)):
#     print(스트레이키즈[i])