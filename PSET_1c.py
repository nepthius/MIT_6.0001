import random
annual_salary = float(input("Enter your annual salary: "))
portion_saved = 1
total_cost = 1000000
epsilon = 100
semi_annual_raise = 0.07
total_cost *= 0.25
current_savings = 0
monthly_salary = annual_salary/12
r = 0.04
high = 10000
low = 0
counter = 0
m = 0

while m<=36:

    current_savings += monthly_salary*portion_saved
    current_savings += current_savings*r/12

    m+=1

    if m%6 == 0:
        monthly_salary *= (1+semi_annual_raise)

    #if(m == 181):
       # print("total before is: ", current_savings)

if current_savings > total_cost:
    while (abs(total_cost - current_savings) > epsilon):

        #print("in the first while loop")
        m = 0
        current_savings = 0
        monthly_salary = annual_salary/12

        portion_saved = (random.randrange(low, high))/10000
        #print("portion_saved: ", portion_saved)

        while m<=36:
            #print("m: ", m)

            current_savings += monthly_salary*portion_saved
            current_savings += current_savings*r/12

            m+=1

            if m%6 == 0:
                monthly_salary *= (1+semi_annual_raise)

            #if(m == 181):
            # print("total before is: ", current_savings)

        if current_savings > total_cost:
            high = int(portion_saved*10000)
        elif current_savings < total_cost:
            low = int(portion_saved*10000)
        
        #print("counter: ", counter)
        counter += 1
    print("Best savings rate: ", portion_saved)
    print("Steps in bisection search: ", counter)

else:
    print("It is not possible to pay the down payment in three years.")
#print("Current total: ", current_savings)
#print("monthly salary: ", monthly_salary)
#print("r is: ", r)





