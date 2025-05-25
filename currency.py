#Conversion of Currency
colombia_pesos = int(input('What do you have left in pesos? : '))
peruvian_soles = int(input('What do you have left in soles? : '))
brazilian_reais = int(input('What do you have left in reais? : '))
total_amt_left = (colombia_pesos* 0.00024 + peruvian_soles* 0.27 + brazilian_reais*0.18)
print('Total amount left in USD is:')
print(total_amt_left)

