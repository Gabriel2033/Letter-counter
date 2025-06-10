# Gabriel Hernandez
# CH 7 Programming assingment
# Part A

# Create a program in a file named letter_count.py.
# Prompt the user to enter three different words or phrases, one at a time; store each response in a separate variable.
# Next, prompt the user a letter they wish to count.
# Finally, count how many times the letter occurs in each of the three words/phrases,
# regardless of case (uppercase or lowercase), as well as the total; output a formatted table displaying the results.
# Be sure your program includes adequate directions for the user.

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