# Print a formatted price list with a given width
item_price = {
    'Apples': 0.4,
    'Pears': 0.5,
    'Cantaloupes': 1.92,
    'Dried Apricots (16 oz.)': 8,
    'Prunes (4 lbs.)': 12
}

width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)

# Iterate and print key/value pairs
for item, price in item_price.items():
    print(fmt.format(item, price))

print('=' * width)
