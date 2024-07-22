# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
print(grades)
grades.reverse()
print(grades)

# 2. Advanced Slicing Techniques

#Task 1 giving the list of temperatures

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperature = temperatures[7:15]
print(second_week_temperature)

# Task 2: Extract all the temperatures above 100 (reminder: when slicing to the end of a list you don't need a stop index).

high_temperature = temperatures[-7:]

print(high_temperature)

# Task 3: extract temperatures from the 5th to the 10th.

day_of_the_month = temperatures[5:10]
print(day_of_the_month)