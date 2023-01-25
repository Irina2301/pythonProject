per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму вклада:")
money = int(money)
deposit = []
deposit = [(round(money*5.6/100)), (round(money*5.9/100)), (round(money*4.28/100)), (round(money*4.0/100))]
print(deposit)
max(deposit)
print(max(deposit))
print("Максимальная сумма, которую вы сможете заработать - "+str(max(deposit)))














