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


""" Find the longest strings """


def longest_string():
    input_array = input('Enter comma separated words (ex: aba, aa, ad, vcd, aba ').split(',')
    input_array = [str(word.strip()) for word in input_array]
    max_word = 0
    for word in input_array:
        if len(word) > max_word:
            max_word = len(word)
    result = []
    for word in input_array:
        if len(word) == max_word:
            result.append(word)
    print(f'The longest word/s in {input_array} is/are {result}')


""" How many matching characters are in two different words """

def repeated():
    word1 = str(input('Enter one word: '))
    word2 = str(input('Enter a second word: '))
    match = 0
    letter_match = []
    for letter in word1:
        if letter in word2:
            if letter not in letter_match:
                letter_match.append(letter)
    for letter in letter_match:
        cant1 = word1.count(letter)
        cant2 = word2.count(letter)

        if cant1 > cant2:
            match += cant2
        else:
            match += cant1
    print(f'There are {match} characters both in {word1} and {word2}')


""" 'Cut' a number in two and check if each half digits add the same """

def sum_half():
    while True:
        try:
            num_string = input('Enter a number with even digits (ex: 45, 4563, or 789635): ')
            len_string = len(num_string)
            if len_string % 2 != 0:
                raise Exception
            half_string1 = num_string[0:int(len_string / 2)]
            half_string2 = num_string[int(len_string / 2):]
            n1_sum = 0
            n2_sum = 0
            for num1 in half_string1:
                n1_sum += int(num1)
            for num2 in half_string2:
                n2_sum += int(num2)
            if n1_sum == n2_sum:
                print(f'The sum of the digits in {half_string1} is equal to the sum of the digits in {half_string2}. '
                      f'They add {n1_sum}')
                break
            else:
                print(f'The sum of the digits in {half_string1} is not the same as the sum of the digits in '
                      f'{half_string2}')
                break
        except:
            print('Try again. Remember to enter a number with an even number of digits.')


""" Rearrange the given numbers in ascending order without changing the position of negative numbers """

def rearrange():
    while True:
        try:
            nums = input('Enter comma separated values (ex: -1, 150, 190, 170, -2, -1, 160, 180): ').split(',')
            nums = [int(num.strip()) for num in nums]
            neg_nums = []
            for i in range(len(nums)):
                if nums[i] < 0:
                    neg_nums.append(i)
            new_nums = []
            for num in nums:
                if 0 <= num:
                    new_nums.append(num)
            new_nums.sort()
            for neg in neg_nums:
                new_nums.insert(neg, nums[neg])
            print(f'Rearranged numbers without moving negative ones: {new_nums}')
            break
        except:
            print('Try again. Enter comma separated values (ex: -1, 150, 190, 170, -2, -1, 160, 180)')


""" Given a list of people's weight, calculate the total weight of two teams considering people will be split into Team1 
and Team 2, one by one """


def get_weight(team):
    weight = 0
    for person in team:
        weight += person
    return weight


def team_weight():
    while True:
        try:
            weights = input("Enter people's weight (ex: 50, 60, 60, 45, 70): ").split(',')
            weights = [int(w.strip()) for w in weights]
            team1 = []
            team2 = []
            for i in range(len(weights)):
                if i % 2 == 0:
                    team1.append(weights[i])
                else:
                    team2.append(weights[i])
            w_team1 = get_weight(team1)
            w_team2 = get_weight(team2)
            print(f'Team 1 {team1} weights {w_team1} and Team 2 {team2} weights {w_team2}')
            break
        except:
            print("Try again. Remember to enter people's weight as comma separated values (ex: 50, 60, 60, 45, 70)")


""" Add a '*' border to a matrix created of same length words """

def add_border():
    while True:
        try:
            matrix = input('Enter same length words separated by comma (ex: abc, ded): ').split(',')
            matrix = [w.strip() for w in matrix]
            new_matrix = []
            for word in matrix:
                if len(word) != len(matrix[0]):
                    raise Exception
                new_word = '*' + word + '*'
                new_matrix.append(new_word)
            len_new_words = len(new_matrix[0])
            ast_string = ''
            for i in range(len_new_words):
                ast_string += '*'
            new_matrix.insert(0, ast_string)
            new_matrix.append(ast_string)
            print(f"Here's your new matrix:")
            for line in new_matrix:
                print(line)
        except:
            print('Try again. Remember to enter same length words (ex: abc, ded')


""" Given two sets of elements, check if sets are equal by swapping 0 to 1 pair of numbers in one of them """


def equal_lists():
    while True:
        try:
            elems1 = input('Enter the first set of elements, separated by comma (ex: 1, 2 ,3): ').split(',')
            elems1 = [elem.strip() for elem in elems1]
            elems2 = input('Enter the second set of elements, separated by comma (ex: 2, 1, 3): ').split(',')
            elems2 = [elem.strip() for elem in elems2]
            if len(elems1) != len(elems2):
                raise Exception
            no_match = []
            for i in range(len(elems1)):
                if elems1[i] != elems2[i]:
                    no_match.append(i)
            if len(no_match) == 0:
                print('You can get equal sets by swapping 0 to 1 pair of elements.')
                break
            elif len(no_match) == 2:
                if elems1[no_match[0]] == elems2[no_match[1]] and elems1[no_match[1]] == elems2[no_match[0]]:
                    print('You can get equal sets by swapping 0 to 1 pair of elements.')
                    break
                else:
                    print("There's no way of getting equal sets by swapping 0 to 1 pair of elements.")
                    break
            else:
                print("There's no way of getting equal sets by swapping 0 to 1 pair of elements.")
        except:
            print('Try again. Remember to enter comma separated values and equal amount of elements each time')


""" Minimal number of changes required to obtain an increasing sequence by only increasing a number by 1 on each 
change """


def min_changes():
    while True:
        try:
            nums = input('Enter comma separated values (ex: 1, 1, 1): ').split(',')
            nums = [int(num.strip()) for num in nums]
            moves = 0
            for i in range(1, len(nums)):
                if nums[i] <= nums[i-1]:
                    dif = nums[i-1] - nums[i] + 1
                    moves += dif
                    new_num = nums[i] + dif
                    nums.pop(i)
                    nums.insert(i, new_num)
            print(f'You can obtain an increasing sequence in {moves} moves if in each move you increase a number by 1.')
            break
        except:
            print('Try again. Remember to enter comma separated values (ex: 1, 2, 4).')


""" Can the letters of a word be rearranged to convert said word to a palindrome? """


def rearrange_palindrome():
    input_string = input('Enter a word: ').lower()
    letter_count = {}
    for letter in input_string:
        try:
            if letter_count[letter]:
                pass
        except KeyError:
            letter_count[letter] = input_string.count(letter)
    odds = 0
    for value in letter_count.values():
        if value % 2 != 0:
            odds += 1
    if odds > 1:
        print(f'Letters in {input_string} cannot be rearrange to get a palindrome.')
    else:
        print(f'Letters in {input_string} can be rearrange to get a palindrome.')


def main():
    print("\nEvery function has its own code, matching the line where its definition starts.")
    print("\nPlease enter the code of the function you want to try: \n")

    my_funcs = (
        (4, 'Add two numbers together', add),
        (19, 'Get century of given year', century),
        (40, 'Check if input is a palindrome', palindrome),
        (54, 'Find pair of adjacent elements with largest product', max_product),
        (74, 'Find area of polygon created by adding n squares of side length = 1 to the rims of an initial '
             'equal square, side by side', area),
        (94, 'How many items are needed to sort a list of items from smallest to biggest so that each item is bigger '
             'than the previous one by exactly 1', arranged_items),
        (116, 'Check if sequence is strictly increasing by only removing 0 to 1 elements', increasing),
        (147, 'Given a rectangular matrix, return the sum of every number that is not 0 or positioned below a 0',
         matrix_sum),
        (179, 'Find the longest strings', longest_string),
        (193, 'How many matching characters are in two different words', repeated),
        (215, "'Cut' a number in two and check if each half digits add the same", sum_half),
        (246, 'Rearrange the given numbers in ascending order without changing the position of negative numbers',
         rearrange),
        (279, "Given a list of people's weight, calculate the total weight of two teams considering people will be "
              "split into Team1 and Team 2, one by one", team_weight),
        (301, "Add a '*' border to a matrix created of same length words", add_border),
        (328, 'Given two sets of elements, check if sets are equal by swapping 0 to 1 pair of numbers in one of them',
         equal_lists),
        (361, "Minimal number of changes required to obtain an increasing sequence by only increasing a number by 1 "
              "on each change", min_changes),
        (383, 'Can the letters of a word be rearranged to convert said word to a palindrome?', rearrange_palindrome)
    )

    for func in my_funcs:
        print(f'{func[0]}. {func[1]}')

    while True:
        try:
            func_num = int(input('\nTry function number: '))
            for func in my_funcs:
                if func[0] == func_num:
                    call_func = func[2]
                    return call_func()
        except:
            print('Please enter a valid function number.')


if __name__ == '__main__':
    main()
