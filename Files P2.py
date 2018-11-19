#Program header goes here

#Declare constants
DIET_DATA = "Dieters.txt"
WT_LOSS_DATA = "WeightLoss.txt"

#Define main function
def main():
    #Open input file
    diet_file = open(DIET_DATA, 'r')

    #Open output file
    wt_loss_file = open(WT_LOSS_FILE, 'w')

    #Try to read data from our file
    name = diet_file.readline().rstrip('\n')

    #Initialize values
    total_loss = 0
    coutn = 0
    
    #Loop through the input file
    while name != '':
        #Read start weight
        start = int(diet_file.readline())

        #Read end weight
        end = int(diet_file.readline())

        #Calculate individual loss
        loss = start - end

        #Calculate overall weight loss
        total_loss += loss

        #Count number of dieters
        count += 1

        #Write person's data to file
        wt_loss_file.write(name + " lost " + str(loss) + " pounds.\n")

        #Read the next name
        name = diet_file.readline().rstrip('\n')

    #Close files
    diet_files.close()
    wt_loss_file.close()

    #Print final values
    print("The", count , "people dieting lost a total of", total_loss, "pounds.")

#Call main function
    main()
