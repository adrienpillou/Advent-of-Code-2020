import requests
import sys
import time

if len(sys.argv) == 1:
	day = int(time.strftime( '%d', time.gmtime()))
	month = int(time.strftime('%m', time.gmtime()))
	year = int(time.strftime('%Y', time.gmtime()))
	if month != 12:
		print("You need to wait \'til December of this year !")
		exit(0)
	if day == 25:
		print("Happy Chritmas !")
	if day > 25:
		print("Chritmas already passed !")
		exit(0)

elif len(sys.argv) == 2:
	day = int(sys.argv[1])
	year = int(time.strftime('%Y', time.gmtime()))

elif len(sys.argv) > 2:
	year, day = int(sys.argv[1]), int(sys.argv[2]) # Year, day

elif len(sys.argv) > 3:
    print('Wrong number of arguments')
    exit(0)

cookie = ""
headers = {'session': cookie}

url = f'https://adventofcode.com/{year}/day/{day}/input'

session = requests.Session()
resp = session.get(url,cookies=headers)

in_file = open(f'day{day:02}.txt','w')
in_file.write(resp.text)
in_file.close()

print(f"Puzzle input of day {day:02} successfully written in file 'day{day:02}.txt'.")
