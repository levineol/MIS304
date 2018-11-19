STUDENTS_FILE = 'StudentNames.txt'

def read_file():
    student_data = open(STUDENTS_FILE, 'r')
    count = 0
    student = student_data.readline().rstrip('\n')
    while student != "":
        print(student)
        count += 1
        student = student_data.readline().rstrip('\n')
    return count
def main():
    number = read_file()
    print("There were", number, "students in the file")
main()
