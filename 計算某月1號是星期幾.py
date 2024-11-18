def get_start_day(year, month):
    if month==1 or month==2:
        month=month+12
        year=year-1
        day=(1+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)+(5*(year//100)))%7
        return int((day+5)%7)
    else:
        day=(1+(13*(month+1)/5)+(year%100)+((year%100)/4)+((year//100)/4)+(5*(year//100)))%7
        return int((day+5)%7)
if __name__=='__main__':
    print(get_start_day(2023,11))