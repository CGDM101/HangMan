# List, string
# function (random select)
# variable assignmnetn (max failure)
# function call (input)
#if, while etc (check if letter is in word)
#array, comparison (if yes)
# print, operation (if not)
# while (repeat/iterate)
#print (result)

import random
guess_count = 0
chances_left = 5

# -----hint-----
list_L=[]
list_L=["Aa", "Bb", "Cc"]
#print(list_L)
#print(list_L[0])
#print("the first element in the list is: ")
#print(list(list_L[0]))

# lenght
length = len(list_L)
#print("length_", length)

random.shuffle(list_L)
#print(list_L)

# =====================
# ==== hangman ========
# =====================
Word_List =["programming", "coding", "software"]
print("Word_List", Word_List)

random.shuffle(Word_List)
print(Word_List)

answer = list(Word_List[0])
print("answer", answer)

display=[]
display.extend(answer)
print("display", display)

used =[]
used.extend(answer)
print("used", display)

# for
for i in range(len(display)):
    display[i] = "-"
print("display", display)
print(" ".join(display))

# while
j = 0
while j<5:
    #j = j+1
    j +=1
    print("j", j)

# input
Variable_a = input("Please guess a letter: ")

# if
if 1==1: # 1==2 kommer det stå no
    print("yes")
else:
    print("no!")

#

