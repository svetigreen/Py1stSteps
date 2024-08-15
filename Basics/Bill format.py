# Print a formatted price list with a given width
item_price = {
    'Apples': 0.4,
    'Pears': 0.5,
    'Cantaloupes': 1.92,
    'Dried Apricots (16 oz.)': 8,
    'Prunes (4 lbs.)': 12,
    'Banana': 0.7
}

width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)

# Sort, Iterate and print key/value pairs
for item in sorted(item_price.keys()):
    print(fmt.format(item, item_price[item]))

# Print the number of items
print('-' * width)
print(header_fmt.format('Number of items', len(item_price)))

print('=' * width)
