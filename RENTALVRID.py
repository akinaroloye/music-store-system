import subscriptionManager as subm
import feedbackManager as feedm
import datetime as dt
from random import randint #Use to create a unqiue ID TO DISTINGUISH different copies of the same music record 

subscriptions = subm.load_subscriptions()
feedback_list = feedm.load_feedback()
def ValidateSUB():
    #Use this to check if the user is subscribed
    global ValidateUserSUB
    global userID
    ValidateUserSUB = True
    while True:
        userID = input("What is your unique customer ID: ")
        if len(userID) != 4:
            print("Your userID can only be 4 characters long. Try again!")
        else:
            if subm.check_subscription(userID, subscriptions) == True: #"User", subscriptions in bracket
                print("Login successful! Welcome", userID)
                ValidateUserSUB = True
                break
            else:
                print("UserID \'{}\' wasn\'t recognised. Try again!".format(userID))
    
def ValidateRID(): #Maybe offer to show all record IDS? Could also do def ValidateRID(RecordID):
    while True:
        global ValidatedRecID
        global RecordID
        ValidatedRecID = False
        RecordID = input("Please enter the unique 5 digit ID of the record you'd like to rent / return: ")
        if len(RecordID) != 5:
            print("Your RecordID can must be 5 characters long. Try again!")
        else:
            f = open("Music_info.txt", "r").readlines()
            while True:
                for line in f:
                    line = line.split(",")
                    if line[0] == RecordID:
                        print("RecordID found")
                        ValidatedRecID = True
                        break
                break
            if ValidatedRecID == False:
                print("RecordID \'{}\' wasn\'t found. Try again!".format(RecordID))
            else:
                break

def musicRent(): #Need to consider subscription limit of the user check by looping through rental.txt and see how many lines have that user ID
    ValidateSUB()
    ValidateRID()
    updatedRentals = []
    date = str(dt.datetime.now().date())
    dateAdj = date.split("-")
    count = 0
    m = open("Rental.txt", "r").readlines()
    for line in m:
        tempStore = line.split(",")
        if tempStore[2].strip() == "" and tempStore[3].strip() == userID:
            count += 1 #Used to count the number of records the User is actively renting 

    q = open("Subscription_Info.txt", "r").readlines()
    for line in q:
        tempStore = line.split(",")
        if tempStore[0] == userID:
            rentalLimit = subm.get_rental_limit(tempStore[1])
        
    dateAdj2 = [int(dateAdj[0]), int(dateAdj[1]), int(dateAdj[2])]
    year, month, day = dateAdj[0], dateAdj[1], dateAdj[2]
    if ValidatedRecID == True and ValidateUserSUB == True and count < rentalLimit: #Prob dont need the two booleans
        f = open("Rental.txt", "r").readlines()
        for line in f:
            tempSearch = line.split(",") 
            if tempSearch[0] == RecordID: #Update rentalcustomer id in rental.txt, change lowercase / uppercase
                if tempSearch[2].strip() == "": #Might be unnecessary as last line should suffice?
                    print("The record ID \'{}\' is actively being rented! Try again another time.".format(RecordID))
                    updatedRentals.append(line)
                else:
                    ReturnDate = tempSearch[2].split("-")
                    ReturnDate2 = [int(ReturnDate[0]), int(ReturnDate[1]), int(ReturnDate[2])]
                    b1 = dt.date(dateAdj2[0], dateAdj2[1], dateAdj2[2])
                    b2 = dt.date(ReturnDate2[0], ReturnDate2[1], ReturnDate2[2])
                    if b1 > b2:
                        print("You can rent this record!")
                        updatedRentals.append("{},{}, ,{}\n".format(RecordID, date, userID)) 
                    else:
                        print("The record ID \'{}\' is actively being rented! Try again another time.".format(RecordID))
                        updatedRentals.append(line)
            else:
                updatedRentals.append(line)
        with open("Rental.txt", "w") as q:
            q.writelines(updatedRentals)
        print("Successfully rented the recordID: {} as of: {}".format(RecordID, date))
    else:
        print("The users has reached their rental limit ({}). Return one before renting again!".format(rentalLimit))
    
    #print(Validated)
#Search for music based on artist, title, medium or genre
#Read MusicInfo, use .split to convert each line to an array, reference items location in array
def musicSearch():
    #y = False
    foundMatch = False
    f = open("Music_Info.txt", 'r').readlines()
    #while y == False:
    search = input("Enter an Artist, Title, Medium or Genre: ")
    for row in f:
        x = row.split(',')
        for i in range(6):
            if x[i-1].lower() == search.lower():
                foundMatch = True
                print("We found a record with:\n\nArtist Name: {}\nTitle: {}\nMedium: {}\nGenre: {}\n".format(x[1], x[2], x[3], x[4])) #Make more pretty
    if foundMatch == False:
        print("No matches were found in our database! ")
                    #x = True
        #if x != True:
            #y = False
                
#MusicSearch()
#Make caps not matter
#Remove \n
#Use .strip to make spaces not matter
def musicReturn():
    updatedRentals = []
    date = str(dt.datetime.now().date())
    ValidateRID()
    f = open("Rental.txt", "r").readlines()
    for line in f:
        tempSearch = line.split(",") 
        if tempSearch[0] == RecordID:
            if tempSearch[2].strip() == "":
                updatedRentals.append("{},{},{},{}\n".format(RecordID,tempSearch[1],date,userID))
            else:
                print("This record isn\'t returnable!")
        else:
            updatedRentals.append(line)
    with open("Rental.txt", "w") as q:
        q.writelines(updatedRentals)
    #THESE SHOULD COME AT END
    StarRating = int(input("Please provide a star rating based on your rental (1-5): "))
    OptFeedback = input("If you'd like to leave a comment about your experience, leave it here. If not, please enter simply press [ENTER] on your keyboard: ")
    if OptFeedback.strip() == "": #This is kinda unnecessary, check its purpose again
        OptFeedback = "N/A"
    feedm.add_feedback(RecordID,StarRating,OptFeedback, "Music_Feedback.txt")
    print("Successfully returned the recordID: {} as of: {}".format(RecordID, date))


def invPrune():
    #Check if return date is more than 14 days from the current date
    f = open("Rental.txt", "r").readlines()
    date = dt.datetime.now().date()
    updatedRentals = []
    for line in f:
        tempStore = line.split(",")
        if tempStore[2].strip() != "" and tempStore[0] != "RecordID":
            rentalDate = dt.datetime.strptime(tempStore[2], "%Y-%m-%d").date()
            if (date-rentalDate).days >= 28:
                toPrune = input("The record {} hasnt been rented in at least 4 weeks, should it be removed? [y/n]: ".format(tempStore[0]))
                if toPrune == "n":
                    updatedRentals.append(line)
                else:
                    print("Successfully pruned the record:", tempStore[0])
            else:
                updatedRentals.append(line)
        else:
            updatedRentals.append(line)
            
    with open("Rental.txt", "w") as f:
        f.writelines(updatedRentals)
                    
def main():
    #Where all functionms will be called
    #Could get  RecordID here and change every other function to def musicReturn(RecordID):
    print("MAIN")


#For pruning, check the length of the file, one that many items have been rented, check which rentaldate is the earliest to prune?

