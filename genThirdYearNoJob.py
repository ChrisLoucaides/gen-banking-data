import random
import pandas as pd
from random import choice
import numpy

def main():
    columns = ['What is your primary UK bank?', 'Do you have a job?', 'Are you a UK, EU/International student?', 'Are you a first, second, or third year student?', 'Number of store discounts', 'Cashback', 'Overdraft', 'What is your exchange limit?', "Good customer service?", 'Importance Exchange rate : Customer Service', 'Importance Exchange rate : Extra Benefits', 'Importance Exchange rate : Online banking', 'Customer Service : Online Banking', 'Importance Customer Service : Extra Benefits', 'Importance Extra Benefits : Online Banking']
    banks = {
        #Bank : weight
        'Monzo': [0.15],
        'Revolut': [0.14],
        'Starling': [0.05],
        'Lloyds': [0.18],
        'Barclays': [0.17],
        'Natwest': [0.12],
        'Nationwide': [0.14],
        'HSBC': [0.04],
        'Santander': [0.1]
    }


    nationalities = ['UK', 'EU/International']
    importance = ['Important', 'Not Important']

    df = pd.DataFrame(columns=columns)


    for i in range(10):
        bank_list = [bank for bank in banks]
        weights = [banks[bank][0] for bank in banks]
        bank = random.choices(bank_list, weights=weights)
        nationality = random.choice(nationalities)
        df.loc[i] = [bank[0], 'No', nationality, 'Third Year', numberOfStoreDiscounts(bank[0]), cashback(bank[0]), overdraft(bank[0]), exchangeLimit(bank[0]), customerService(bank[0]), exchangeRateToCustomerService(bank[0], nationality), exchangeRateToBenefits(bank[0], nationality), exchangeRateToOnlineBanking(bank[0], nationality), customerCareToOnlineBanking(bank[0]), customerCareToExtraBenefits(bank[0]), onlineBankingToExtraBenefits(bank[0])]

    df.to_csv('thirdYearNoJob.csv')

def customerService(bank): #generate quality of customer service
    if random.randint(0, 1) == 0:
        return "Yes"
    else:
        return "No"

def overdraft(bank):
    if bank == "Revolut":
        return 0
    else:
        chance = random.randint(0,10)
        if chance < 4:
            return random.randrange(100, 500, 10)
        return 0

def numberOfStoreDiscounts(bank):
    if bank == "Lloyds":
        chance = random.randint(0,10)
        if chance > 7:
            return random.randint(0,19)
        else:
            return random.randint(0,6)

    elif bank == "Barclays":
        chance = random.randint(0,5)
        if chance == 0:
            return random.randint(2,4)
        else:
            return random.randint(0,2)

    elif bank == "Monzo":
        return random.randint(0,3)

    elif bank == "Revolut":
        return random.randint(0,5)

    elif bank == "Natwest": #https://www.natwest.com/myrewards/partner-retailers.html#earn
        return random.randint(0,20)

    elif bank == "Santander":
        return random.randint(0,5)

    elif bank == "Starling":
        chance = random.randint(0,2)
        if chance == 0:
            return random.randint(1,3)
        else:
            return random.randint(0,1)
    else:
        return random.randint(0,1)

def exchangeLimit(bank):
    if bank == "Monzo":
        return "Unlimited"
    elif bank == "Revolut":
        return 1000
    elif bank == "Lloyds":
        return 0
    elif bank == "Barclays":
        return 0
    elif bank == "Natwest":
        return 0
    elif bank == "Starling":
        return "Unlimited"
    elif bank == "HSBC":
        return 0
    elif bank == "Nationwide":
        return "Unlimited"
    elif bank == "Santander":
        return 0

def cashback(bank):
    if bank == "Monzo":
        return 0.3
    elif bank == "Revolut":
        return 0
    elif bank == "Lloyds":
        return 0
    elif bank == "Barclays":
        return 0
    elif bank == "Natwest":
        return 0
    elif bank == "Starling":
        return 0
    elif bank == "HSBC":
        return 0
    elif bank == "Nationwide":
        return 0
    elif bank == "Santander":
        return 0

def exchangeRateToCustomerService(bank, nationality):

    if bank == "Revolut" or nationality == "EU/International":
        if(random.randint(0,7) < 1):
            return "It's the same"
        elif random.randint(0,1) == 0:
            return "Important"
        else:
            return "Very Important"
    else:
        chance = random.randint(0,11)
        if chance >= 0 and chance < 3:
            return "Very important"
        elif chance >= 3 and chance < 5:
            return "Important"
        elif chance >= 5 and chance < 7:
            return "It's the same"
        elif chance >=7 and chance <= 10:
            return "Not important"
        else:
            return "Absolutely not important"

def exchangeRateToBenefits(bank, nationality):
        if bank == "Revolut" or nationality == "EU/International":
            if(random.randint(0,7) < 1):
                return "It's the same"
            elif random.randint(0,1) == 0:
                return "Important"
            else:
                return "Very Important"
        else:
            chance = random.randint(0,16)
            if chance >= 0 and chance < 8:
                return "Very important"
            elif chance >= 8 and chance < 12:
                return "Important"
            elif chance >= 12 and chance < 14:
                return "It's the same"
            elif chance >=14 and chance <= 15:
                return "Not important"
            else:
                return "Absolutely not important"

def exchangeRateToOnlineBanking(bank, nationality):
        if bank == "Revolut" or bank == "Monzo" or nationality == "EU/International":
            if(random.randint(0,7) < 1):
                return "It's the same"
            elif random.randint(0,1) == 0:
                return "Important"
            else:
                return "Very Important"
        else:
            chance = random.randint(0,14)
            if chance >= 0 and chance < 3:
                return "Very important"
            elif chance >= 3 and chance < 5:
                return "Important"
            elif chance >= 5 and chance < 7:
                return "It's the same"
            elif chance >=7 and chance <= 13:
                return "Not important"
            else:
                return "Absolutely not important"

def customerCareToOnlineBanking(bank):
    chance = random.randint(0,99)
    if chance >= 0 and chance <=19:
        return "Very Important"
    elif chance <= 20 and chance <= 34:
        return "Important"
    elif chance <=35 and chance <= 49:
        return "It's the same"
    elif chance <=50 and chance <= 79:
        return "Not important"
    else:
        return "Absolutely not imporant"

def customerCareToExtraBenefits(bank):
    chance = random.randint(0,99)
    if chance >= 0 and chance <= 39:
        return "Very important"
    elif chance >= 40 and chance <= 69: #kek
        return "Important"
    elif chance >= 70 and chance <= 89:
        return "It's the same"
    elif chance >=90 and chance <= 95:
        return "Not important"
    else:
        return "Absolutely not important"

def onlineBankingToExtraBenefits(bank):
    chance = random.randint(0,99)
    if chance >= 0 and chance <= 59:
        return "Very Important"
    elif chance >= 60 and chance <= 79:
        return "Important"
    elif chance >=80 and chance <= 89:
        return "It's the same"
    elif chance >= 90 and chance <= 97:
        return "Not Important"
    else:
        return "Absolutely not Important"

main()
