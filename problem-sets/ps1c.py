## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))


#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_house = 800_000
down_payment = cost_of_house*0.25
steps = 0
r_upper_bound = 1
r_lower_bound = 0
best_savings_rate = 0.5



##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# Check whether initial amount is already enough
if initial_deposit >= down_payment:
    best_savings_rate = 0.0
elif initial_deposit*(1+1/12)**36 < down_payment - 100:
    best_savings_rate = None
else:
    while (initial_deposit*(1+best_savings_rate/12)**36 < down_payment - 100 
           or initial_deposit*(1+best_savings_rate/12)**36 > down_payment + 100):
        steps += 1
        if initial_deposit*(1+best_savings_rate/12)**36 < down_payment - 100:
            r_lower_bound = best_savings_rate
            best_savings_rate = (r_upper_bound + r_lower_bound)/2
        else:
            r_upper_bound = best_savings_rate
            best_savings_rate = (r_upper_bound + r_lower_bound)/2

print(f"Best savings rate: {best_savings_rate}")
print(f"Steps in bisection search: {steps}")