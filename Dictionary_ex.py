# A simple database
# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone
# number and address, respectively.
people = {
    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },
    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },
    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}
# Descriptive labels for the phone number and address. These will be used
# when printing the output.
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

# Create a dictionary copy with all lower keys
people_lower_keys = {key.lower(): value for key, value in people.items()}

flag_quit = 'y'
while flag_quit == 'y':
    name = input('Name: ')
    # Are we looking for a phone number or an address?
    request = input('Phone number (p) or address (a)? ')
    # Use the correct key:
    key = request  # In case the request is neither 'p' nor 'a'
    if request == 'p':
        key = 'phone'
    if request == 'a':
        key = 'addr'

    # Use get to provide default values:
    person = people_lower_keys.get(name.lower(), {})
    label = labels.get(key, key)
    result = person.get(key, 'not available')

    # Only try to print information if the name is a valid key in
    # our dictionary:
    print("{}'s {} is {}.".format(name, label, result))

    flag_quit = input('Do you like to look for anything else? (y/n): ')
    match flag_quit:
        case 'n':
            print("Bye bye!")


