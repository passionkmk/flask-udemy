my_variable = "hello"
grades = [77, 80, 90]
tuple_grades = (77, 80, 90) # immutable 불변
set_grades = {77, 80, 90} # unique & unordered

tuple_grades = tuple_grades + (100,) #튜블로 하려면 (100,) 쉼표가 들어가야함
set_grades.add(60)
print(tuple_grades)
print(set_grades)

