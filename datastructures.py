# list data structure
# 1.list are mutable(changeable)
# 2.list are ordered
# 3.list are indexes
# 4.Uses box brackets

fruits = ["apples.", "bananas.", "cherries.", "oranges.", "strawberries.", "pineapples.", "pears." ]
print(fruits)
fruits[2]='watermelons.'
print(f'I love eating ' + fruits[2])

numbers = [1,2,3,4,5,6,7,8,9]
numbers.remove(4)
print(numbers)

# tuples data structure
# 1.tuples are immutable(unchangeable)
# 2.tuples are ordered
# 3.tuples have indexes
# 4.Uses normal brackets

cars = ('BMW ', 'Audi ', 'Subaru ', 'Toyota ', 'Mercedes ', 'Mazda ', 'Nissan ', 'Tesla ')
print(cars[3])
print(len(cars))
nambari = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(len(nambari))


# set data structure
# 1.Set data Uses curly braces
# 2.set data list is not ordered.
# 3.sets do not have indexes
# 4.Sets are unchangeable/immutable

days = {'MOnday', 'Teusday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday'}
print(days)

# dictionaries data structure
# 1.Dictionaries are mutable

students = {'Name': 'John', 'Age':45,'Gender': 'M', 'School': 'eMobilis'}
print(students)
print(students['School'])
print('John studies at ' + students['School'])
