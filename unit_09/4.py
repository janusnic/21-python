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
