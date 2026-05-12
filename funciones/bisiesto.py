def is_year_leap(year):
   if year % 4 != 0:     # Si el año NO es divisible por 4, no puede ser bisiesto
      return False
   elif year % 100 != 0: # Si es divisible por 4 pero si NO es divisible por 100, entonces SÍ es bisiesto
      return True
   elif year % 400 != 0: # Es divisible por 4 y por 100, Si NO es divisible por 400, entonces NO es bisiesto
      return False
   else:                 # Es divisible por 4, 100 y 400, Por lo tanto, SÍ es bisiesto
      return True

def days_in_month(year, month):
   if year < 1582 or month < 1 or month > 12:
      return None
   days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   result = days[month - 1]
   if month == 2 and is_year_leap(year):
      return 29
   return result

def day_of_year(year, month, day):
   limit = days_in_month(year, month)
   if limit is None or day < 1 or day > limit: 
      return None
   total_days = day
   for m in range(1, month):
      total_days += days_in_month(year,m)
   return total_days


print(day_of_year(2000, 12, 31))
print(day_of_year(2026, 5, 16))


print("="*50)



'''
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
   yr = test_years[i]
   mo = test_months[i]
   print(yr, mo, "->", end="")
   result = days_in_month(yr, mo)
   if result == test_results[i]:
      print(f"OK {test_results[i]}")
   else:
      print("Fallido")
'''