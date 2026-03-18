
name = "Nabeel Ahmad"
age = 26
drinks_coffee = True
salary = 10000.50

print(f"My name is {name}, I am {age} years old.")
print(f"Do I drink coffee? {drinks_coffee}")
print(f"My salary is Rs. {salary:,.2f}")

retirement_age = 60
years_until_retirement = retirement_age - age
print(f"\nYears until retirement at {retirement_age}: {years_until_retirement}")

cups_per_day = 3
cost_per_cup = 150
days_per_week = 7
weekly_coffee_budget = cups_per_day * cost_per_cup * days_per_week
print(f"Weekly coffee budget (3 cups/day at Rs. {cost_per_cup} each): Rs. {weekly_coffee_budget:,.2f}")


print(f"\nIn {years_until_retirement} years, I will spend Rs. {weekly_coffee_budget * 52 * years_until_retirement:,.2f} on coffee!")
