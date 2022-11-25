class Coins:
    def __init__(self, country, coin, code_coin):
        self.country = country
        self.coin = coin
        self.code_coin = code_coin

        
    def print(self):
        print("La moneda de "+ self.country +" es: "+ str(self.coin)+ "\nY su codigo es: "+ str(self.code_coin))

    # def change(self):
    #     coin = input("Ingrese la nueva moneda: ")
        
