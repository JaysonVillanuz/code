#ask the user to inputname
name = input("Enter your name: ")

#print the name
print(name)

#Ask the user for prelim grade
prelim_grade = int(input("Enter Prelim Grade: "))
#print the prelim_grade 
print(prelim_grade)

#Askthe user for midterm grade
midterm_grade = int(input("Enter the Midterm Grade: "))
#print the midterm grade
print(midterm_grade)

#Askthe user for final grade
final_grade = int(input("Enter Final Grade: "))
#print the final gradr
print(final_grade)

#formula for average
average_grade = (prelim_grade * 0.3) + (midterm_grade * 0.3) + (final_grade * 0.4)

#print the student name
print("Student Name: ",name)
#print the average grade
print("Average Grade: ",average_grade)
