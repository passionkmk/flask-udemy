my_variable = "hello"
grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable 불변
set_grades = {77, 80, 90} # unique & unordered

tuple_grades = tuple_grades + (100,) #튜블로 하려면 (100,) 쉼표가 들어가야함
set_grades.add(60)
# print(tuple_grades)
# print(set_grades)

## Set operation

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

# print(your_lottery_numbers.intersection(winning_numbers)) # 교집합
# print(your_lottery_numbers.union(winning_numbers)) # 합집합
print({1, 2, 3, 4}.difference({1, 2}))