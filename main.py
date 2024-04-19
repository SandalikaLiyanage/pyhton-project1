#collecting user inputs(deposits and the bet)
# 1.to get the user deposit

#this is a global constant, which should be in all capitals( for the code to be nice and dynamic)
MAX_LINES =3
MAX_BET=100
MIN_BET=1

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

# collect the bets from the user(how much they want to bet, and how many lines they want to bet on, then can multiply the bet amount by lines)
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