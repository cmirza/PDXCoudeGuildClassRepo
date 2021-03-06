'''
Lab 17 - Number to Phrase
'''


def num2phrs(num):

    # define list of numbers 1-19
    words1 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    # define list of decade numbers
    words2 = ['Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

    tens_digit = num // 10  # floor division to get tens digit
    ones_digit = num % 10  # remainder to get ones digit

    if 1 <= num < 19:  # if number is between 1-10, select corresponding word from words1 list
        return words1[num-1]  # return corresponding word
    elif 20 <= num <= 99:  # if number is between 20-99, select corresponding decade number with tens digit and combine with corresponding number with ones_digit
        return words2[tens_digit-2] + words1[ones_digit-1]  # return combined words
    else:  # otherwise return error
        print("Invalid number.")


number = input('Enter a number between 0-99: ')  # prompt for a number from 0-99
print(num2phrs(int(number)))  # pass number to function
