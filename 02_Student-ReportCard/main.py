name=input("Enter your Full name: ")
num=int(input("Enter number of subjects: "))
total=0
for i in range(1, num + 1):
    marks = float(input(f"Enter marks for subject {i}: "))
    total += marks

percentage = (total / (num * 100)) * 100
if(percentage>=90):
    grade="A+"
    print("Congratulations! Grade=A+")
elif(percentage>=80 and percentage<90):
    grade="A"
    print("Congratulations! Grade=A")
elif(percentage>=70 and percentage<80):
    grade="B+"
    print("Congratulations! Grade B+")
elif(percentage>=60 and percentage<70):
    grade="B"
    print("Congratulations! Grade=B")
elif(percentage>=50 and percentage<60):
    grade="C"
    print("Congratulaions! Grade=C")
else:
    grade="Fail"
    print("Sorry you are Failed")

print("\n--------STUDENT REPORT CARD--------")
print("Student Name:",name)
print(f"Total Marks  : {total}/{num*100}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")