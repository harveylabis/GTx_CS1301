#Defines function "currencyAmount"
def currencyAmount(currency, amount): 
    if currency == "JPY":
        return "¥" + str(amount)
    elif currency == "USD":
        return "$" + str(amount)
    elif currency == "GBP":
        return "£" + str(amount)
    else:
        return str(amount)

#Prints currencyAmount(5)'s output
#print(currencyAmount(5))    


