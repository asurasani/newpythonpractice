#Question 7: Print the following pattern using for loop
def question_seven():
    rows = 5
    for i in range(0, rows + 1):
        for j in range(rows - i, 0, -1):
            print(j)
        print()
question_seven()

# Question 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

#Question 9: Display -10 to -1 using for loop
for i in range(-10, 0):
    print(i)