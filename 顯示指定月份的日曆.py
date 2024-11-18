def is_leap_year(year):
    if year%400==0:
        return True
    elif year%4==0:
        if year%100==0:
            return False
        else:
            return True

def get_days_in_month(year,month):
    A=[4,6,9,11]
    if month==2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in A:
        return 30
    elif month not in A:
        return 31
def get_start_day(year, month):
    if month==1 or month==2:
        month=month+12
        year=year-1
        day=(1+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)+(5*(year//100)))%7
        return int((day+5)%7)
    else:
        day=(1+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)+(5*(year//100)))%7
        return int((day+5)%7)
def display_calendar(year,month):
    A=[]
    print('    ',year,'年',month,'月')
    print('Mo Tu We Th Fr Sa Su')
    for i in range(get_start_day(year, month)):
        A.append(' ')
        
    for i in range(1, get_days_in_month(year, month)+1):
        A.append(i)
    
    for i in range(len(A)):
        print('%2s' %(A[i]), end=' ')
        
        if (i+1)%7==0:
            print()


display_calendar(2024, 11)