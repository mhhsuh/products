products = []
while True:
	name = input('please enter the name of product: ')
	if name == 'q':
		break
	price = input('please enter the price of product: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'cost', p[1], 'dollars')