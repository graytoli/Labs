# Lab 24: Rain Data, version 1
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

def main():
    local_rain_data = grab_raindata('rain_table.txt')
    for tup in local_rain_data:
        print(tup)
        print(date_as_int(tup[0]))

main()
