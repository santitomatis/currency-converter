menu = """
Welcome! This is your currency converter
1- convert from USD to ARS
2- convert from ARS to USD
3- convert from USD to MX
4- convert from MX to USD

Type <1> <2> <3> <4> according to the convert action required (without using <>)"""
print(menu)
convert = int(input(""))
value_ARS_USD = 0.004878
value_USD_ARS = 205
value_MX_USD = 0.050
value_USD_MX = 20

def converter(currency_to_convert, value_currency, currency_output):
    print("How many " + currency_to_convert + " do you have?")
    to_convert = int(input(""))
    converted = round(to_convert * value_currency)
    print("You got about " + str(converted) + " " + currency_output)

if convert == 1:
    currency_to_convert = "USD"
    currency_output = "ARS"
    converter(currency_to_convert, value_USD_ARS, currency_output)

if convert == 2:
    currency_to_convert = "ARS"
    currency_output = "USD"
    converter(currency_to_convert, value_ARS_USD, currency_output)

if convert == 3:
    currency_to_convert = "USD"
    currency_output = "MX"
    converter(currency_to_convert, value_USD_MX, currency_output)

if convert == 4:
    currency_to_convert = "MX"
    currency_output = "USD"
    converter(currency_to_convert, value_MX_USD, currency_output)


else:
    print("invalid command, execute again and type properly")
