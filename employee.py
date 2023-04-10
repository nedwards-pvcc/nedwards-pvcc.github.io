import datetime


category_codes = ("C", "S", "J", "M")
hourly_pay_rates = (16.50, 15.75, 15.75, 19.50)
deduction_rates = (0.12, 0.03, 0.062, 0.0145)

while True:
 
    category_code = input("Enter job category code (C, S, J, or M): ")
    hours_worked = float(input("Enter number of hours worked: "))

 
    category_index = -1
    for i in range(len(category_codes)):
        if category_code.upper() == category_codes[i]:
            category_index = i
            break

   
    if category_index == -1:
        print("Invalid job category code")
        continue

   
    pay_rate = hourly_pay_rates[category_index]
    federal_income_tax = deduction_rates[0]
    state_income_tax = deduction_rates[1]
    social_security_tax = deduction_rates[2]
    medicare_tax = deduction_rates[3]

    
    gross_pay = pay_rate * hours_worked
    federal_income_tax = gross_pay * federal_income_tax
    state_income_tax = gross_pay * state_income_tax
    social_security_tax = gross_pay * social_security_tax
    medicare_tax = gross_pay * medicare_tax
    total_deductions = federal_income_tax + state_income_tax + social_security_tax + medicare_tax
    net_pay = gross_pay - total_deductions

    
    print("\nEmployee Payroll Information")
    print(" Mega Corp Ware.inc ")
    print("----------------------------")
    print(f"Hours worked: {hours_worked:.2f}")
    print(f"Gross Pay : ${gross_pay:>8.2f}")
    print(f"Federal Income Tax : ${federal_income_tax:>8.2f}")
    print(f"State Income Tax : ${state_income_tax:>8.2f}")
    print(f"Social Security Tax : ${social_security_tax:>8.2f}")
    print(f"Medicare Tax : ${medicare_tax:>8.2f}")
    print(f"Total Deductions : ${total_deductions:>8.2f}")
    print(f"Net Pay : ${net_pay:>8.2f}")
    print(datetime.datetime.now())
    
    another_employee = input("Would you like to input data for another employee? (y/n): ")
    if another_employee.lower() == "n":
        break


print("\nProgram terminated.")

