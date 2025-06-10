

first_word = input('Enter the first word').lower()
second_word = input('Enter the second word').lower()
third_word = input('Enter the third word').lower()

letter_count = input('Enter the letter you to count')
print('occurences of',letter_count)


print('-' * 34)
print(f'{first_word:<16}{first_word.count(letter_count):>16}')
print(f'{second_word:<16}{second_word.count(letter_count):>16}')
print(f'{third_word:<16}{third_word.count(letter_count):>16}')
print('-' * 34)

total = print('Total', first_word.count(letter_count)+ second_word.count(letter_count)+ third_word.count(letter_count))
