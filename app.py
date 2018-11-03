import matplotlib as matplotlib

print("python\"3.7")

print(max(-4.5,-2.5))

phrase="Python"

print(phrase.upper())

print(phrase.lower())

coordinates=(4,5), (5,6), (80,34)

print(coordinates[0])

num1 = "50.4"

num2 = "46.3"

result = float(num1)+float(num2)

print(result)

name=["horse", "slackware", "sentinel", "rogue"]

print(name[-4])

name.append("kalilinux")

name.remove("rogue")

name.insert(3,"morgan")

print(name)

monthconversion={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

print(monthconversion["Jan"])

print(monthconversion.get("Abc","Not a valid key"))

i=1
while i<=100:
    print(i)
    i += 1

print("Done with the loop")

number_grid= [
    [4,5,6],
    [1,2,3],
    [7,8,9],
    [0]
]

print(number_grid[2][1])

open("AABA_2006-01-01_to_2018-01-01.csv", "r")

open("movie_metadata.csv", "r")

monthconversion={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December"
}

file=open('movie_metadata.csv', encoding="utf8")

import csv
import numpy
filename = 'movie_metadata.csv'
raw_data = open(filename, 'rt', encoding='utf8')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x=list(reader)
data = numpy.array(x).astype('object')
print(data.shape)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5],[6,2,9,1,3])
plt.xlabel='Result'
plt.show()

