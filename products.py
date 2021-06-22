products = []
while True:
	name = input('please enter the name of product: ')
	if name == 'q':
		break
	price = input('please enter the price of product: ')
	price = str(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'cost', p[1], 'dollars')

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,Price,unit\n')
	for p in products:
		f.write(p[0]+ ','+ p[1] + ',' + 'dollar' + '\n')
