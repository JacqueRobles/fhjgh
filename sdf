from monedas import Coins

def main():
    coin_list = []
    while (True):
        op = input("(1)Ingresar nueva moneda \n(2)Cambiar moneda \n(3)Salir \n")
        if (op =="1"):
            country = input("Ingrese el pais de la moneda: ")
            coin = input("Ingrese la moneda: ")
            code_coin = input("Ingrese el codigo de la moneda: ")
            coins = Coins(country, coin, code_coin)
            coins.print()
            coin_list.append(coins)
            
        elif (op =="2"):
            for i in range(len(coin_list)):
                print(coin_list[i])
        elif (op == "3"):
            break
    
main()
