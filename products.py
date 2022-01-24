import os # operating system

# Read File
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'Item, Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return products

# Prompt User to input
def user_input(products):
	while True:
		name = input('Please enter the item name: ')
		if name == 'q':
			break
		price = input('Please enter the item price: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

# Print all purchase record
def print_products(products):
	for p in products:
		print('The price of', p[0], 'is', str(p[1]) + '.')

# Write file
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('Item, Price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # Check whether file exist
		print('Yeah! Find the file!')
		products = read_file(filename)
	else:
		print('No such a file.')

	products = user_input(products)
	print_products(products)
	write_file(filename, products)

main()


