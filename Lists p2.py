#Program header

#Define main function
def main():
    #Create list
    magical_list = [1, 2, 3, 4, 5]

    #Assign second list
    unicorn_list = []

    #Assign first list values to second list
    for fairy in magical_list:
        unicorn_list.append(fairy)
        
    #Initialize index
    index = 0

    #Change values in magical_list
    for fairy in magical_list:
        #Calculate new value
        fairy = fairy * 10

        #Assign new value to existing spot
        magical_list[index] = fairy

        #Increment index
        index += 1

    #Print lists
    print("Magical list", magical_list, "Unicorn list", unicorn_list)

#Call main function
main()

def main2():
    num_list = [1,2,3]
    manip_list(num_list)
    print(num_list)

def manip_list(list_a):
    index = 0
    for n in list_a:
        list_a[index] = n + 1
        index += 1

main2()

    
