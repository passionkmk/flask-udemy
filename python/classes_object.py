lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LottteryPlayer: 
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LottteryPlayer("Rolf")
player_one.name = (1, 2, 3, 6, 7, 8)
player_two = LottteryPlayer("Jose")

# print(player_one.name == player_two.name)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avarage(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to {}.".format(self.school))

    @classmethod
    def must_go_to_school(cls):
        print("I must go to school. I don't care anymore!")

    @staticmethod
    def finally_go_to_school():
        print("Finally. I'm go to school.")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
anna.marks.append(71)
# anna.go_to_school()
anna.must_go_to_school()
anna.finally_go_to_school()
Student.finally_go_to_school()

# rolf.go_to_school()
# rolf.must_go_to_school()
        