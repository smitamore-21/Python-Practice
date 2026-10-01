# Calculate simple interest using the formula: SI = (P * R * T) / 100.

# P = Principal → original amount
# R = Rate → interest rate in percentage
# T = Time → time period, usually in years
# SI = Simple Interest


P = int(input("Enter principal : "))
R = int(input("Enter rate : "))
T = int(input("Enter time : "))

# Formula: SI = (P * R * T) / 100
SI = (P * R * T) / 100

# Display simple interest
print("Simple interest is :", SI)