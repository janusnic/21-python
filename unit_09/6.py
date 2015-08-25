with open('examples/test.log', mode='w', encoding='utf-8') as a_file:
	a_file.write('test succeeded')

with open('examples/test.log', encoding='utf-8') as a_file:
	print(a_file.read())

with open('examples/test.log', mode='a', encoding='utf-8') as a_file:
	a_file.write('test succeeded again')

with open('examples/test.log', encoding='utf-8') as a_file:
	print(a_file.read())
