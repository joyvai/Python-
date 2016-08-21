"""  

if (year is not divisible by 4) then (it is a common year)
else if (year is not divisible by 100) then (it is a leap year)
else if (year is not divisible by 400) then (it is a common year)
"""

def is_leap_year2(year):
	if year % 4 == 0:
		return True

	elif year % 100 == 1 :
		return False
		
	elif year % 400 == 0:
		return  True
	
	else:
		return False

def test_is_leap_year():
	years = [1900, 2000, 2001, 2002, 2020, 2008, 2010,2016]

	for year in years:
		if is_leap_year2(year):
			print year, 'is leap year.'
		else:
			print year, 'is not a leap year'

test_is_leap_year()
