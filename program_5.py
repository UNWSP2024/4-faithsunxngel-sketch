# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

# PSEUDOCODE 
# start
#    prompt user for budget amount
#    set total_expenses = 0
#
#    while user has more expenses to enter
#        prompt user for an expense
#        add expense to total_expenses
#        ask if they want to enter another expense

#    calculate difference = budget - total_expenses

#    if difference > 0
#        display "You are under budget by", difference
#    else IF difference < 0
#        display "You are over budget by", absolute value of difference
#    else
#        display "You are exactly on budget!"
#end


def main():
    budget = float(input("Enter the amount budgeted for this month: $"))
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    while spent != 0:
        spent = float(input("Enter an expense (0 to quit): $"))
        total += spent
    difference = budget - total

    print("\nBudget Analysis")
    print("-----------------")
    print(f"Total budget: ${budget:.2f}")
    print(f"Total expenses: ${total:.2f}")

    if difference > 0:
        print(f"You are under budget by ${difference:.2f}")
    elif difference < 0:
        print(f"You are over budget by ${abs(difference):.2f}")
    else:
        print("You are exactly on budget!")

        


if __name__ == '__main__':
    main()