#  Marksheet App
  
rollno = int(input("Enter your roll number:"))
name = input("Enter your name:")
standard = input("Enter your standard:")
english = int(input("Enter your marks in English:"))
urdu = int(input("Enter your marks in Urdu:"))
islamiat = int(input("Enter your marks in Islamiat:"))
maths = int(input("Enter your marks in Maths:"))
physics = int(input("Enter your marks in Physics:"))
chemistry = int(input("Enter your marks in Chemistry:"))

obtained_marks = english + urdu + islamiat + maths + physics + chemistry
percentage = (obtained_marks / 600) * 100

print("------------------Student Marksheet------------------")
print("Roll Number:", rollno)
print("Name:", name)
print("Standard:", standard)
print("Total Marks: 600")
print("Marks Obtained:", obtained_marks)
print("Percentage:", percentage)

if percentage >= 80:
    print("Grade: A+")
    print("Remarks: Excellent 👏")
elif percentage >= 70:
    print("Grade: A")
    print("Remarks: Very Good 👍")
elif percentage >= 60:
    print("Grade: B")
    print("Remarks: Good 👌")
elif percentage >= 50:
    print("Grade: C")
    print("Remarks: Average 😐")
elif percentage >= 40:
    print("Grade: D")
    print("Remarks: Need Improvement 😕")
elif percentage >= 33:
    print("Grade: E")
    print("Remarks: Work Hard 😞")
else:
    print("Grade: F")
    print("Remarks: Fail 😭")                   
       



