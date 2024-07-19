while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        value = x / y
        print(f'{x} / {y} =', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again.')
        print()
    else:
        break  # the loop is broken only when no exception is raised.
    finally:
        print("Cleaning up.")  # guarantee that the finally-clause will be executed,
        # no matter what exceptions occur in the try clause. Useful e.g. for closing files or network sockets
