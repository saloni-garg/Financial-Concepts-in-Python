import numpy as np

# Derive the equivalent monthly mortgage rate from the annual rate
mortgage_rate_periodic = ((1+0.0375)**(1/12) - 1)

# How many monthly payment periods will there be over 30 years?
mortgage_payment_periods = 30*12

# Calculate the monthly mortgage payment (multiply by -1 to keep it positive)
periodic_mortgage_payment = -1*np.pmt(rate=mortgage_rate_periodic, nper=12*30, pv=640000)
print("Monthly Mortgage Payment: " + str(round(periodic_mortgage_payment, 2)))