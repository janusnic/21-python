filename = 'examples/portfolio.csv'
a_file = open(filename)
a_str = a_file.read()
print(a_str)
print(a_file.name)
print(a_file.encoding)
print(a_file.mode)
