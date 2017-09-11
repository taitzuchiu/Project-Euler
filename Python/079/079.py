def main():
    guesses = read_file("num.txt")
    before = {}
    after = {}

    #Get digits used in each passcode guess
    digits = get_digits(guesses)

    #Creates dictionary entry for each unique number in passcode.
    for num in digits:
        before[num] = []
        after[num] = []

    #Iterate over each guess.
    for guess in guesses:
        for i in range(0,3):
            for j in range(0,3):
                #Places digits in before/after dictionary based on digit position.
                if (i < j and guess[j] not in after[guess[i]]):
                    after[guess[i]] += guess[j]
                elif (i > j and guess[j] not in before[guess[i]]):
                    before[guess[i]] += guess[j]

    print(get_passcode(digits, before, after))

""" Function that opens file and returns an array of passcode guesses. """
def read_file(filename):
    file = open(filename, "r")
    array = file.read().splitlines()
    file.close()
    return array

""" Reads file to find out all unique digits used in the passcode """
def get_digits(guesses):
    digits = []
    for guess in guesses:
        for digit in guess:
            if digit not in digits:
                digits += digit
    return digits

""" Iterates over 'before' and 'after' dictionaries to check how many numbers appear
    before and after each digit. Returns the correct passcode. """
def get_passcode(digits, before, after):
    length = len(digits)
    passcode = ""
    for i in range(0, length):
        for num in digits:
            # Checks if digit in the correct position based on before/after len.
            if (len(before[num]) == i and len(after[num]) == length - 1 - i):
                passcode += num
    return passcode

main()
