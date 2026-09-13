## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter the starting yearly salary: "))
portion_saved = float(input("Enter a portion saved (as a decimal between 0 and 1): "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annnual_raise = float(input("Enter your semi annual raise rate: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
months = 0
amount_saved = 0
portion_down_payment = 0.25
r = 0.05

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

# Add additional condition that checks if semi-year is reached, then only change yearly_salary
while (cost_of_dream_home*portion_down_payment > amount_saved):
    months += 1
    amount_saved += (yearly_salary*portion_saved)/12 + (amount_saved*(r/12))
    if months%6 == 0:
        yearly_salary += yearly_salary*semi_annnual_raise

print(f"Number of months to save for down payment on dream house: {months}")
