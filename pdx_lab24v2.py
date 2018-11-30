# Lab 24: Rain Data, version 2
import datetime

def grab_raindata(table):
    with open(table) as file:
        rows = file.read().split('\n')
    rain_per_day = []
    for i in range(4, len(rows)):
        daily_data = rows[i].split()
        rain_per_day.append(tuple([daily_data[0]] + [daily_data[1]]))
    return rain_per_day

def date_as_int(date):
    return datetime.datetime.strptime(date, '%d-%b-%Y')

def max_rainfall(some_list):
    amounts_list = []
    for tup in some_list:
        amounts_list.append(tup[1])
    max_num = max(amounts_list)
    num_idx = amounts_list.index(max_num)
    max_day = some_list[num_idx]
    return max_day

def year_max(some_list):
    year_totals = {}
    for tup in some_list:
        year = date_as_int(tup[0]).year
        search_year = year_totals.get(year)
        if search_year == None and tup[1] != '-':
            year_totals[year] = int(tup[1])
        elif tup[1] != '-':
            year_totals[year] += int(tup[1])
    return max(year_totals, key=year_totals.get)

def main():
    local_rain_data = grab_raindata('rain_table.txt')
    for tup in local_rain_data:
        print(tup)
        print(date_as_int(tup[0]))
    max_day = max_rainfall(local_rain_data)
    print(f"{max_day[0]} was the day with the most recorded rainfall since 1998 at {max_day[1]} inches of rainfall.")
    print(f"{year_max(local_rain_data)} was the year recorded with the most rainfall.")

main()
