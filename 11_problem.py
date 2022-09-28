'''
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

Solution

nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
What was the temperature on Jan 9?
What was the temperature on Jan 4?
Figure out data structure that is best for this problem

Solution

poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
 'diverged': 2,
 'in': 3,
 'I': 8
Solution

Implement hash table where collisions are handled using linear probing. We learnt about linear probing in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use linear probing. Keep MAX size of arr in hashtable as 10.
Solution
'''

# What was the average temperature in first week of Jan
arr = []
with open('E:\Python\CodeBasics\DataStrcture\weather.csv', 'r') as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temparature. Ignore the row")

print(arr)

avg_temp = sum(arr[0:7]) / len(arr[0:7])
print(avg_temp)

# What was the maximum temperature in first 10 days of Jan
max_temp = max(arr[0:10])
print(max_temp)
f.close()

# What was the temperature on Jan 9?
weather = {}
with open("E:\Python\CodeBasics\DataStrcture\weather.csv", 'r') as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather[day] = temperature
        except:
            print("Invalid date and temperature")

print(weather)

print(weather['Jan-09'])
print(weather['Jan-04'])

##########################################################
with open('E:\Python\CodeBasics\DataStrcture\poem.txt', 'r') as f:
    word_count = {}
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            if word not in word_count.keys():
                word_count[word] = 1
            else:
                word_count[word] += 1

print(word_count)
