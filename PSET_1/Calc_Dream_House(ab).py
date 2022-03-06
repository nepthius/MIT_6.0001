annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save as a decimal: "))
total_cost = float(input("Enter the total cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
total_cost *= 0.25
portion_down_payment = 0
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04
m = 0
counter  = 0

while current_savings < total_cost:

    current_savings += monthly_salary*portion_saved
    current_savings += current_savings*r/12

    m+=1

    if m%6 == 0:
        monthly_salary *= (1+semi_annual_raise)

    #if(m == 181):
       # print("total before is: ", current_savings)

#print("Current total: ", current_savings)

print("Number of months: ", m)
