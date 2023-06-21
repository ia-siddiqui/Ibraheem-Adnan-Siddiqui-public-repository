#Program allowing user access to two financial calculators:
#investment calculator and a home loan calculator

import math

#Introducing the options to the user
print("\nInvestment - to calculate the amount of interest you'll earn on your investment")
print("Bond - to calculate the amount you'll have to pay on a home loan \n")

#The user must choose which calculator they want to use

selection = input("Enter either 'Investment' or 'Bond' from the menu above to proceed: ")
#To ensure variable selection is homogenous, so capitals don't affect it, we use .title
selection = selection.title()

# As a test, we can use print(selection) to check the .title is working correctly

#Here, we use if, elif and else to enact the calculator based on their choice
if (selection == "Investment"): #Condition 1: Investment calculator has been chosen

    #The following values cannot be stored as strings, as they are needed for 
    #further calculation
    #Float is used for the amount because monetary values can go to 2 decimal places
    initial_deposit_amount = float(input("How much are you depositing initially? £"))
    interest_rate = (int(input("What is the interest rate(Whole number): ")))/100
    number_years_investing = int(input("How many years are you investing? "))

    #Now you want to ask whether they want to calculate simple or compound interest
    interest_type = input("Do you want to calculate 'simple' or 'compound' interest? ")
    #To ensure variable interest_type is homogenous, so capitals don't affect it, we use .title
    interest_type = interest_type.title()

    if (interest_type == "Simple"): #Condition 1: Calculating value with simple interest
        
        value_after_interest = initial_deposit_amount *(1 + (interest_rate * number_years_investing))

        #Rounding the value to 2 decimal points as we are dealing with currency, which is 2dp
        #Got this from https://www.geeksforgeeks.org/how-to-round-numbers-in-python/
        value_after_interest = round(value_after_interest, 2)

        print(f"\nValue after interest: \t£{value_after_interest}")
        
    elif(interest_type == "Compound"): #Condition 2: Calculating value with compound interest
        
        #Calculating the value after compound interest
        value_after_interest = initial_deposit_amount * math.pow((1 + interest_rate), number_years_investing)

        #Rounding the value to 2 decimal points as we are dealing with currency, which is 2dp
        #Got this from https://www.geeksforgeeks.org/how-to-round-numbers-in-python/
        value_after_interest = round(value_after_interest, 2)

        print(f"\nValue after interest: \t£{value_after_interest}")

    elif (len(interest_type) == 0):  #Condition 3: User has not entered anything
        
        print("You have not entered anything")

    else: #User has entered an invalid input
        
        print("Invalid input")
    
elif (selection == "Bond"): #Condition 2: Bond calculator has been chosen
    
    #The following values cannot be stored as strings, as they are needed for 
    #further calculation
    #Float and round are used for the value because monetary values can go to 2 decimal places
    present_house_value = round(float(input("Please input the present value of your house: £")), 2)

    annual_interest_rate = (int(input("What is the yearly interest rate: ")))/100
    #Calculating the monthly interest rate requires dividing by 12
    monthly_interest_rate = annual_interest_rate / 12

    number_months_for_repayment = int(input("Over how many months do you plan to repay the bond? "))

    #Calculate monthly repayments
    monthly_repayment_value = (monthly_interest_rate * present_house_value)/(1- (1 + monthly_interest_rate)**(-number_months_for_repayment))
    
    #Rounding the value to 2 decimal points as we are dealing with currency, which is 2dp
    #Got this from https://www.geeksforgeeks.org/how-to-round-numbers-in-python/
    monthly_repayment_value = round(monthly_repayment_value, 2)

    print(f"\nMonthly repayment value: \t£{monthly_repayment_value}")
    

elif (len(selection) == 0):  #Condition 3: User has not entered anything
    print("You have not entered anything")

else: #User has entered an invalid input
    print("Invalid input")
