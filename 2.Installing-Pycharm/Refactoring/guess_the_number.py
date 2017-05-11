import random

NUMBER_OF_GUESSES = 5
RANGE_TOP = 20
RANGE_BOTTOM = -10


def get_input():
    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_GUESSES):
        guess = int(raw_input('guess the number: '))
        if guess == random_number:
            print 'well done'
            break
        elif -10 > guess or guess > 20:
            print "Not in Range, try again!"
        elif guess > random_number:
            print "too high, guesses left: " + str(NUMBER_OF_GUESSES - i - 1)
        else:
            print "too low guesses left: " + str(NUMBER_OF_GUESSES - i - 1)


while True:
    # generate the random number
    random_number = random.randint(RANGE_BOTTOM, RANGE_TOP)

    print "Pick a number between " + str(RANGE_BOTTOM) + " and " + str(RANGE_TOP)
    get_input()

    print "let's try a new number!"