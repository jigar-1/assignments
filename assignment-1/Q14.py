from datetime import date

d1 = date.fromisoformat(input("Enter date1 (YYYY-MM-DD): "))
d2 = date.fromisoformat(input("Enter date2 (YYYY-MM-DD): "))
print("Days between:", abs((d2 - d1).days))