import random
import pandas as pd
from random import choice
import numpy

def main():
    columns = ['What is your primary UK bank?', 'Do you have a job?', 'Are you a UK, EU/International student?', 'Are you a first, second, or third year student?', 'How important is the exchange limit?', 'How helpful is the customer service?', '1 - Student discounts at stores', '2 - Transport', '3 - Cashback', '4 - Overdraft', '5- Other', '1 - App', '2 - Website', 'What is your Exchange Limit?', 'What is your overdraft amount?', 'How much is the average cashback you receive?']
    banks = {
        #Bank : weight
        'Monzo': [0.35],
        'Revolut': [0.25],
        'Starling': [0.15],
        'Lloyds': [0.08],
        'Barclays': [0.05],
        'Natwest': [0.04],
        'Nationwide': [0.03],
        'HSBC': [0.03],
        'Santander': [0.02]
    }


    nationalities = ['UK', 'EU/International']
    importance = ['Important', 'Not Important']

    df = pd.DataFrame(columns=columns)


    for i in range(10):
        bank_list = [bank for bank in banks]
        weights = [banks[bank][0] for bank in banks]
        bank = random.choices(bank_list, weights=weights)
        nationality = random.choice(nationalities)
        curImportance = currencyImportance(nationality, bank)
        df.loc[i] = [bank, 'No', nationality, 'First Year', curImportance, random.randint(1, 5), random.choice(importance), random.choice(importance), random.choice(importance), random.choice(importance), 'NA', random.choice(importance), random.choice(importance), 0, 0, 0]

    df.to_csv('test.csv')

def currencyImportance(nationality, bank): #Generate importance of currency exchange depending on nationality/bank
    if nationality == "EU/International":
        ###########Revolut users would be more likely to give a higher number for currency exchange importance ##########
        if bank == 'Revolut':
            chance = random.randint(1,7)
            if chance > 1:
                return random.randint(3,5)
            else:
                return random.randint(1,3)
        else:
            chance = random.randint(1, 7)
            if chance == 1:
                return random.randint(4,5)
            return random.randint(1,3)
        ###########Revolut users would be more likely to give a higher number for currency exchange importance ##########
        chance = random.randint(1,4)
        if chance > 1:
            return random.randint(3,5)
        else:
            return random.randint(1,3)
    else:
        chance = random.randint(1,8)
        if chance == 1:
            return random.randint(4,5)
        else:
            return random.randint(1,3)


def customerService(bank): #generate importance of customer service
    if bank == "Monzo" or bank == "Revolut":
        return 2 + random.randint(0,1)
    elif bank == "Lloyds" or bank == "Barclays" or bank == "Natwest" or bank == "HSBC" or bank == "Nationwide" or bank == "Santander":
        return 4 + random.randint(0,1)
    else:
        return 3 + random.randint(0,1)

def overdraft(bank):
    if bank == "Revolut":
        return 0
    else:
        chance = random.randint(0,10)
        if chance < 4:
            return random.randrange(100, 500, 10)
        return 0


main()
