# Calculate the future value of the investment and print it out
future_value = 100*(1+0.06)**30
print("Future Value of Investment: " + str(round(future_value, 2)))

# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(pow((1+(growth_rate)),growth_periods))
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*((1+growth_rate)**growth_periods)
print("Future value: " + str(round(future_value, 2)))

