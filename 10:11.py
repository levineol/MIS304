#program

#Define main fucntion
def main():
    #Declare list
    num_list = [5, 10, 15, 20, 25]

    #Initialize index
    index = 0
    
    #Loop to process values
    for num in num_list:
        #Double the value
        num = num * 2

        #Update element of list
        num_list[index] = num

        #Print new value from list
        print(num_list[index])

        #Increment index
        index += 1

    #Print entire list
    print(num_list)

main()
