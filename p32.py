import emp

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

da_amt = emp.da(basic)
hra_amt = emp.hra(basic)
pf_amt = emp.pf(basic)
tax_amt = emp.tax(basic)

gross = basic + da_amt + hra_amt
net = gross - pf_amt - tax_amt

print("\n--- Salary Slip ---")
print("Name:", name)
print("Basic Salary:", basic)
print("DA:", da_amt)
print("HRA:", hra_amt)
print("PF:", pf_amt)
print("Tax:", tax_amt)
print("Gross Salary:", gross)
print("Net Salary:", net)
