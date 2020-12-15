# 2.Write an if statement to determine whether a variable holding a year isa leap year
def checkyear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));
year = 2000
if(checkyear( year)):
    print("leap Year")

else:
    print("Not a leap year")