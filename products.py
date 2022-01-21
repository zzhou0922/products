import os # operating system

# Read File
products = []
if os.path.isfile('products.csv'): # Check whether file exist
	print('Yeah! Find the file!')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'Item, Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('No such a file.')

# Prompt User to input
while True:
	name = input('Please enter the item name: ')
	if name == 'q':
		break
	price = input('Please enter the item price: ')
	price = int(price)
	products.append([name, price])
print(products)

# Print all purchase record
for p in products:
	print('The price of', p[0], 'is', str(p[1]) + '.')

# Write file
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Item, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

