#Program Hader

#Declare constants
STUDENT_NAMES = "MoreStudentNames.txt"
STUDENT_NAMES_AND_GRADES = "StudentsAndGrades.txt"

#define main function
def main():
    #open input file
    student_input = open(STUDENT_NAMES, 'r')

    #Open output file
    student_output = open(STUDENT_NAMES_AND_GRADES, 'w')

    #Loop to read data from file and write output to new file
    for student in student_input:
        #Remoce newline from student name
        student = student.rstrip("\n")

        #Prompt user for test grade
        grade = int(input("Please enter the grade for " + student + ": "))

        #Write student name and grade to output file
        student_output.write(student + ", " + str(grade) + "\n")

    #Close input file
    student_input.close()

    #Close output file
    student_output.close()



for blank in range
    read
    total+=q1
