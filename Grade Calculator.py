english = float(input(" Please enter English Marks: "))
math = float(input(" Please enter Math score: "))
computers = float(input(" Please enter Computer Marks: "))
physics = float(input(" Please enter Physics Marks: "))
chemistry = float(input(" Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
percentage = float(total / 500) * 100

print("Total Marks = %.2f"  %total)
print("Marks Percentage = %.2f"  %percentage)

if(percentage >= 90)and(percentage <= 100):
    print("A Grade")
elif(percentage >= 80)and(percentage <= 89):
    print("B Grade")
elif(percentage >= 70)and(percentage <= 79):
    print("C Grade")
elif(percentage >= 60)and(percentage <= 69):
    print("D Grade")
elif(percentage >= 40)and(percentage <= 59):
    print("E Grade")
else:
    print("Fail")