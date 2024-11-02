#use of if else statement
#show the student is pass or fail

#input the marks of student
marks = int (input("Enter the marks: "))

#check the condition
if marks >= 40 and marks <50:
    print("You are pass & you got 'D' grade")
elif marks >=50 and marks <60:   
    print("You are pass & you got 'c' grade")
    
elif marks >=60 and marks <70:
    print("You are pass & you got 'B' grade")
elif marks >=70 and marks <80:
    print("You are pass & you got 'A' grade")
elif marks >=80 and marks <90:
    print("You are pass & you got 'A+' grade")
else:
    print("You are fail")