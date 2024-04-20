#to generate slot machine numbers randomly

import random

#collecting user inputs(deposits and the bet)
# 1.to get the user deposit

#this is a global constant (for the code to be nice and dynamic), which should be in all capitals
MAX_LINES =3
MAX_BET=100
MIN_BET=1

#set number of rows and columns that we are going to have in slot machine
#imagine you have a 3 by 3 slot machine
ROWS=3
COLS=3

#set the number of symbols in each column
symbol_count={
    "A":2,
    "B":4,
    "c":6,
    "D":8
}

# the outcome of the slot machine using the above values
def get_slot_machine_spin(rows,cols,symbols):
    #generate(randomly) what symbols are gonna be in each column based on the frequency of the symbols that we have 
    #randomly pick the number of rows inside of each column
    #to do that , create a list that contains all of the different values possibly could select from, and to randomly choose 3 of those values(and after we choose one, we need to remove it from the list and choose again)
    all_symbols=[]
    #add every symbol in the dictionary into this list using for loop
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #what values are going to every single column
    #each of this nested lists will represents the values in our column
    columns= [] #this is like columns=[ [], [], [] ]
    for _ in range(cols):
        column= []
        #you need a copy of all_symbols (":"->represents copy) list, Because after we selected one symbol we need to remove it before we choose next
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            #now add this value to the column
            column.append(value)
        columns.append(column)    
    
    return columns





def deposit():
    # continuosly ask the user to enter the deposit amount until they give a valid amount
    while True:
        amount=input("What would you like to deposit? $")
        #check whether the the user entered a valid whole number, not a string or anyother
        if amount.isdigit():
            #that number comes as a string initially , so convert it to a number
            amount=int(amount)
            # now check that number is greater than 0 , if yes then break from the loop
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount

# 2. collect the bets from the user(how much they want to bet, and how many lines they want to bet on, then can multiply the bet amount by lines)
# get number of lines
def get_number_of_lines():
    #pick a number between 1 nd 3, because the numberb of lines we have is 3
    while True:
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        #check whether the the user entered a valid whole number, not a string or anyother
        if lines.isdigit():
            #that number comes as a string initially , so convert it to a number
            lines=int(lines)
            # now check that number is within the bound, if yes then break from the loop
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
        
    return lines

#amount that user wanna bet on each line
def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $")
        #check whether the the user entered a valid whole number, not a string or anyother
        if amount.isdigit():
            #that number comes as a string initially , so convert it to a number
            amount=int(amount)
            # now check that number is greater than 0 , if yes then break from the loop
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                #put f before the string , then put {} and give any variable
                print(f"Amount must be between ${MIN_BET}-${MAX_BET}.")
        else:
            print("Please enter a number.")
        
    return amount


# if you want to rerun the program you can call the main function
def main():
    balance = deposit()
    lines=get_number_of_lines()

    #bet should be within the balance amount
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to: ${total_bet}")

    
main()