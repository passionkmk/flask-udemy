# should_continue = True
# if should_continue:
#     print("Hello")
person = ""
while person != "exit":
    knwon_people = ["John", "Anna", "Mary"]
    person = input("Enter the person you know: ")
    if person == "exit":
        print("Correct! You must go out!")
        break

    if person in knwon_people:
        print("You know this person!")
    else:
        print("You don't know this person!")
        
