def get_student_id():

    new_eid = input("Please enter the student's eid: ")
    valid_eid_begin = 0
    valid_eid_end = 0
    
    while valid_eid_begin == 0:
        if new_eid[0:3].isalpha():
            valid_eid_begin = 1
        else:
            new_eid = input("Make sure the first three characters are letters. Please try again: ")
            valid_eid_begin = 0

    while valid_eid_end == 0:
        if new_eid[3:].isdigit():
            valid_eid_end = 1
        else:
            new_eid = input("Make sure the last four characters are digits. Please try again: ")
            valid_eid_end = 0
get_student_id()
