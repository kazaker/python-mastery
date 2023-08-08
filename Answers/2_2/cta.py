import readrides
from collections import Counter

rows = readrides.read_rides_as_dicts('../../Data/ctabus.csv')

# How many bus routes exist in Chicago?

number_of_routes = set()
for x in rows:
    number_of_routes.add(x["route"])

print("# How many bus routes exist in Chicago?")
print(len(number_of_routes))

# Comprehension
len({s['route'] for s in rows})


# How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?

number_of_rides = 0
for y in rows:
    if y["route"] == "22" and y["date"] == "02/02/2011":
        number_of_rides += y["rides"]

print("# How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?")
print(number_of_rides)

# Comprehension
print(sum([s["rides"] for s in rows if s["route"] == "22" and s["date"] == "02/02/2011"]))
print(sum([s["rides"] for s in rows if s["route"] == "22" and s["date"] == "07/17/2012"]))


# What is the total number of rides taken on each bus route?
total_rides = Counter()

for z in rows:
    total_rides[z["route"]] += z["rides"]

print("# What is the total number of rides taken on each bus route?")
print(total_rides)

# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

total_rides_2001 = Counter()
total_rides_2011 = Counter()

for z in rows:
    year = z["date"][-4:]
    if year == "2001":
        total_rides_2001[z["route"]] += z["rides"]
    elif year == "2011":
        total_rides_2011[z["route"]] += z["rides"]


total_growth = Counter()

for key, value in total_rides_2001.items():
    if key in total_rides_2011:
        total_growth[key] += total_rides_2011[key] - value
    
print('# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?')
print(total_growth.most_common(3))