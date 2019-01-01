my_list = [0, 1, 2, 3, 4]

an_equal_list = [x for x in range(5)]

multiply_list = [x * 3 for x in range(5)]
# print(multiply_list)

# print(8 % 3)
# print(9 % 2)

# print([n for n in range(10) if n % 2 == 0])
# print([n % 2 == 0 for n in range(10)])


people_you_know = ["Rolf", "Anna", "Jack", "GREG"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)