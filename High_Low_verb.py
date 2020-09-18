low = 1
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    #print("\t guessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. should I guess higher or lower? "
                     "Enter h or l or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # guess higher. the lower end of the range becomes 1 greater tah  thh e guess
        low =guess + 1
    elif high_low == "l" :
        #guess lower. the highend of the range becvomes one less than the guess
        high = guess -1
    elif high_low == "c":
        print("I got it in {} guesses! I am the best".format(guesses))
        break
    else:
        print("please enter h, l or c")

        #    guesses = guesses +1

    guesses += 1

else:
    print("yes solved it, it is number {}".format(low))
    print("I got it in {} guesses! I am the best".format(guesses))