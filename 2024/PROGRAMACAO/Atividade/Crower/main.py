# Import from the parent directory (app)
import os
polygonKey = os.environ.get("POLYGON_API_KEY")
#Import from the parent directory (app)
import calendar
import datetime
from dotenv import load_dotenv
import holidays
import requests
from time import sleep

import db
from logs.logs import info, error, warn, critic

load_dotenv()

today = datetime.date.today()
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

def start():
    print("Bem vindo ao seu simple home broker!\n")

    def operation():
        db.create_purchases()
        while True:
            financ = int(input("""Qual operação gostaria de fazer?
                1- COMPRAR
                2- VENDER
                3- SAIR\n"""))
            if financ == 1:
                ticker = input("Insira o ticker do ativo que deseja comprar agora (exemplo: AAPL):\n")
                amount = int(input("Insira a quantidade de ativos que deseja comprar:\n"))
                
                if isinstance(ticker, str) and isinstance(amount, int):
                    db.insert(ticker.upper(), amount, now)
                    print("\n\nFeito!\n\n")
                    sleep(3)
                else:
                    print("Algo deu errado, por favor, entre o valor novamente.")
            elif financ == 2:
                ticker = input("Insira o ticker do ativo que deseja vender agora (exemplo: AAPL):\n")
                amount = int(input("Insira a quantidade de ativos que deseja vender:\n"))
                if isinstance(ticker, str) and isinstance(amount, int):
                    db.delete(ticker.upper(), amount, now)
                    print("\n\nFeito!\n\n")
                    sleep(3)
                else:
                    print("Algo deu errado, por favor, entre o valor novamente.")
            elif financ == 3:
                print("Obrigado pela preferência!")
                break
            else:
                print("Não entendi, por favor, digite novamente")
    
    condition = input("Quer consultar as operações financeiras que já havia feito anteriormente? [S/N]\n")

    if condition.upper() == "S":
        results = db.read()
        print(results)

        conditionII = input("Quer efetuar uma operação financeira agora? [S/N]\n")
        if conditionII.upper() == "S":
            operation()

        if conditionII.upper() == "N":
            print("Obrigado pela preferencia, volte sempre!")
            return
            if conditionII.upper() == "S":
                operation()
            elif conditionII.upper() == "N":
                print("Compreendo, espero poder ajudar melhor posteriormente\nObrigado pela preferencia, volte sempre!")
                return
            else:
                print("Acho que não entendi, tente novamente.")
    else:
        print("Obrigado pela preferencia, volte sempre\n")
            

def is_business_day(date):
    # Check if the day is a weekday (Monday=0, Sunday=6)
    if date.weekday() < 5:
        # Check if the day is not a public holiday
        if date not in holidays.CountryHoliday('USA'):
            return True
    return False

def last_business_day(date):
    prev_day = date - datetime.timedelta(days=1)
    while not is_business_day(prev_day):
        prev_day -= datetime.timedelta(days=1)
    return prev_day

today = datetime.date.today()

if is_business_day(today):
    #if today.weekday() == calendar.MONDAY:
    if today.weekday():    
        last_bd = last_business_day(today)
        day = last_bd.strftime('%Y-%m-%d')
        print(f"\nINFORMATIVO: Hoje ({day}) é dia útil\n\n")
    else:
        last_bd = last_business_day(today)
        day = last_bd.strftime('%Y-%m-%d')
        print(f"INFORMATIVO: Hoje ({day}) não é dia útil!")
else:
    last_bd = last_business_day(today)
    day = last_bd.strftime('%Y-%m-%d')
    print(f"INFORMATIVO: O ultimo dia útil foi: {day}")

def getQuote(ticker):
    polygonKey=os.getenv('OBFUSCATE')
    response = requests.get(f"https://api.polygon.io/v1/open-close/{ticker}/{day}?apiKey={polygonKey}")
    if response.status_code == 200:
        # data = response.json()
        # data = json.dumps(data)
        data = response.json()
        print(f"\nQuote result\n\n{data}")
        print(type(data))
        return data
    else:
        print(response.status_code)
        print(response.text)
        return None

if __name__ == "__main__":
    start()