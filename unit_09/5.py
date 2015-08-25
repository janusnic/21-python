filename = 'examples/portfolio.csv'
a_file = open(filename)
a_str = a_file.read()
print(a_str)
print(a_file.name)
print(a_file.encoding)
print(a_file.mode)

print('file seek')
print(a_file.seek(0))
print('file read(16)')
print(a_file.read(16))

print('file read(1)')
print(a_file.read(1))
print('file tell')
print(a_file.tell())

print('file read(1)')
print(a_file.read(1))

print('file tell')
print(a_file.tell())


line_number = 1
with open('examples/favorite-people.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        print('{:>4} {}'.format(line_number, a_line.rstrip()))
        line_number += 1

portfolio = []

# Преобразует строку в список
# Извлекает и преобразует отдельные значения полей

for line in open(filename):
    fields = line.split(",") #
    name = fields[0]
    #
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price) # Создает кортеж (name, shares, price)
    portfolio.append(stock) # Добавляет в список записей

# Каждая строка представлена кортежем и может быть извлечена
print(portfolio[0])

print(portfolio[1])

# Отдельные значения могут извлекаться следующим способом:
print(portfolio[1][1])

print(portfolio[1][2])

# реализовать обход всех записей и распаковать значения полей в набор переменных:

total = 0.0
for name, shares, price in portfolio:
	total += shares*price

print('total= ',total)
