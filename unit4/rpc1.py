#read input.txt file and put it to an array
with open("input.txt") as f:
    lines = f.readlines()

lines = [x.strip() for x in lines] # python list comprehension

# ! Using Arrays
# ! Permutations
# A X --> R R = 1 + 3 = 4
# A Y --> R P = 1 + 0 = 1
# A Z --> R S = 1 + 6 = 7
# B X --> P R = 2 + 6 = 8
# B Y --> P P = 2 + 3 = 5
# B Z --> P S = 2 + 0 = 2
# C X --> S R = 3 + 0 = 3
# C Y --> S P = 3 + 6 = 9
# C Z --> S S = 3 + 3 = 6

# loop through every element of line
# use if else statements to compare the permutations
# have a variable that keeps track of the score
# after every if else statement, add the score to the score
