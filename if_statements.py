# should_continue = True
# if should_continue:
#     print("Hello")
# person = ""
# while person != "exit":
#     knwon_people = ["John", "Anna", "Mary"]
#     person = input("Enter the person you know: ")
#     if person == "exit":
#         print("Correct! You must go out!")
#         break

#     if person in knwon_people:
#         print("You know this person!")
#     else:
#         print("You don't know this person!")
        
# knwon_people = ["John", "Anna", "Mary"]
# person = input("Enter ")

def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    # people_list = people.split(",")
    # people_whithout_space =[]
    # for person in people_list:
    #     people_whithout_space.append(person.strip())
    # return people_list
    return [person.strip() for person in people.split(",")]

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know {}!".format(person))

ask_user()