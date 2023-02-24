""" Add two numbers together """


def add():
    while True:
        try:
            param1 = float(input('Enter one number: '))
            param2 = float(input('Enter another number: '))
            sum = param1 + param2
            print(f'{param1} + {param2} = {round(sum, 2)}')
            break
        except:
            print('Try again. Only numbers are admitted.')


""" Get century of given year """


def century():
    start = 1
    end = 100
    century_nbr = 1
    while True:
        try:
            year = int(input('Enter a year: '))
            while year not in list(list(range(start, end+1))):
                start += 100
                end += 100
                century_nbr += 1
            else:
                print(f'{year} is century {century_nbr}')
                break
        except:
            print('Try again. Enter a valid year (ex: 1998)')


""" Check if input is a palindrome """


def palindrome():
    your_string = input('Enter input text: ')
    new_string = ''
    for i in range(1, len(your_string)+1):
        new_string += your_string[-i]
    if new_string.lower() == your_string.lower():
        print(f'{your_string} is a palindrome. Check it out: {new_string}')
    else:
        print(f'{your_string} is not a palindrome.')


""" Find pair of adjacent elements with largest product """


def max_product():
    while True:
        try:
            input_array = input('Enter comma separated values (ex: 3, 6, -2, -5, 7, 3): ').split(',')
            input_array = [float(num.strip()) for num in input_array]
            products = []
            for i in range(len(input_array)-1):
                product = input_array[i] * input_array[i+1]
                products.append(round(product, 2))
                products.sort()
            print(f'The largest product of a pair of adjacent elements is {products[-1]}')
            break
        except:
            print('Try again. Remember to enter comma separated values (ex: 3, 6, -2, -5, 7, 3).')


""" Find area of polygon created by adding n squares of side length = 1 to the rims of an initial equal square, side by 
side """


def area():
    while True:
        try:
            n = int(input('Enter number of squares to add: '))
            square = n + n - 1
            big_area = square ** 2
            rest = 0
            for i in range(1, n):
                rest += 1
            pol_area = big_area - rest * 4
            print(f'Adding {n} squares to each side of the initial square we get a polygon with area {pol_area}')
            break
        except:
            print('Try again. Enter a (whole) number of squares.')


""" How many items are needed to sort a list of items from smallest to biggest so that each item is bigger than the 
previous one by exactly 1 """


def arranged_items():
    while True:
        try:
            items = input('Enter comma separated values (ex: 6, 2, 3, 8): ').split(',')
            items = [int(num.strip()) for num in items]
            items.sort()
            min_item = items[0]
            max_item = items[-1]
            new_items = []
            for i in range(min_item, max_item+1):
                if i not in items:
                    new_items.append(i)
            print(f'You need {len(new_items)-len(items)} items to arrange {items} so that each item is 1 bigger than the previous '
                  f'one ({new_items})')
            break
        except:
            print('Try again. Remember to enter comma separated values (ex: 3, 6, -2, -5, 7, 3).')


""" Check if sequence is strictly increasing by only removing 0 to 1 elements """


def increasing():
    while True:
        try:
            sequence = input('Enter comma separated values (ex: 1, 3, 2, 1): ').split(',')
            sequence = [int(num.strip()) for num in sequence]
            count = 0
            index = -1
            for i in range(1, len(sequence)):
                if sequence[i - 1] >= sequence[i]:
                    count += 1
                    index = i
            if count > 1:
                print('Sequence is not strictly increasing, even removing 0 to 1 elements.')
                break
            if count == 0:
                print('Sequence is strictly increasing after removing 0 to 1 elements.')
            if index == len(sequence) - 1 or index == 1:
                print('Sequence is strictly increasing after removing 0 to 1 elements.')
            if sequence[index - 1] < sequence[index + 1]:
                print('Sequence is strictly increasing after removing 0 to 1 elements.')
            if sequence[index - 2] < sequence[index]:
                print('Sequence is strictly increasing after removing 0 to 1 elements.')
            print('Sequence is not strictly increasing, even removing 0 to 1 elements.')
            break
        except:
            print('Try again. Remember to enter comma separated values (ex: 1, 3, 2, 1).')


""" Given a rectangular matrix, return the sum of every number that is not 0 or positioned below a 0 """


def matrix_sum():
    while True:
        try:
            rows = int(input('Enter a whole number indicating the number of rows: '))
            cols = int(input('Enter a whole number indicating the number of columns: '))
            matrix = []
            for n in range(1, rows+1):
                new_row = input(f'Enter {cols} comma separated values (ex: 0, 1, 1, 2): ').split(',')
                new_row = [int(num.strip()) for num in new_row]
                if len(new_row) != cols:
                    raise Exception
                else:
                    matrix.append(new_row)
            sum_matrix = 0
            exclude = []
            for m in range(len(matrix)):
                for i in range(len(matrix[0])):
                    if matrix[m][i] == 0:
                        exclude.append(i)
                for n in range(len(matrix[0])):
                    if n not in exclude:
                        sum_matrix += matrix[m][n]
            print(f'The sum of every number that is not 0 or positioned below a 0 in {matrix} is {sum_matrix}.')
            break
        except:
            print('Try again. Remember to enter comma separated values (ex: 1, 3, 2, 1) and that each input has to '
                  'have n numbers matching the number of columns.')


def main():
    print("\nEvery function has its own code, matching the line where its definition starts.")
    print("\nPlease enter the code of the function you want to try: \n")

    my_funcs = [{'nbr': 4, 'name': 'Add two numbers together', 'function': add},
                {'nbr': 19, 'name': 'Get century of given year', 'function': century},
                {'nbr': 40, 'name': 'Check if input is a palindrome', 'function': palindrome},
                {'nbr': 54, 'name': 'Find pair of adjacent elements with largest product', 'function': max_product},
                {'nbr': 74, 'name': 'Find area of polygon created by adding n squares of side length = 1 to the rims '
                                    'of an iitial equal square, side by side', 'function': area},
                {'nbr': 94, 'name': 'How many items are needed to sort a list of items from smallest to biggest so '
                                    'that each item is bigger than the previous one by exactly 1',
                 'function': arranged_items},
                {'nbr': 116, 'name': 'Check if sequence is strictly increasing by only removing 0 to 1 elements',
                 'function': increasing},
                {'nbr': 147, 'name': 'Given a rectangular matrix, return the sum of every number that is not 0 or '
                                     'positioned below a 0', 'function': matrix_sum}]

    for func in my_funcs:
        print(f'{func["nbr"]}. {func["name"]}')

    func_num = int(input('\nTry function number: '))

    for func in my_funcs:
        if func['nbr'] == func_num:
            call_func = func['function']
            call_func()


if __name__ == '__main__':
    main()
