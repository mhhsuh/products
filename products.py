products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Product' in line:
			continue
		name, price, unit = line.strip().split(',')
		# print(name, price)
		products.append([name, price, unit])
print(products)

# user to key-in information
while True:
	name = input('please enter the name of product: ')
	if name == 'q':
		break
	price = input('please enter the price of product: ')
	price = str(price)
	products.append([name, price])
print(products)

#print out all products and price information
for p in products:
	print(p[0], 'cost', p[1], 'dollars')

#write data into file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,Price,unit\n')
	for p in products:
		f.write(p[0]+ ','+ p[1] + ',' + 'dollar' + '\n')
