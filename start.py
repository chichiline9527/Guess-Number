from random import randint

print("Welcome To Play Guess Number Game!")
print("\nYou have to guess the number which between lower bound and upper bound.")

lower_in = input("Type the lower bound: ")
upper_in = input("TYpe the upper bound: ")

ans_lower = int(lower_in)
ans_upper = int(upper_in)

ans = randint(ans_lower, ans_upper)
print("The answer has been generated.")

lower = ans_lower
upper = ans_upper

cnt = 1

g = input("You guess: ")
guess = int(g)

while guess != ans:
    if ans > guess:
        lower = guess
    else:
        upper = guess

    cnt += 1
    
    print "From " + str(lower) + " to " + str(upper) + " ."

    guess = input("You guess: ")

print "Correct Answer!! You guess " + str(cnt) + " times."
