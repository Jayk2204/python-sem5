import employee

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))

da = employee.DA(basic)
hra = employee.HRA(basic)
pf = employee.PF(basic)
itax = employee.ITAX(basic)

gross = basic + da + hra
net = gross - pf - itax

print("Employee Name:", name)
print("Gross Salary:", gross)
print("Net Salary:", net)
