import subscriptionManager as subm
import feedbackManager as feedm
import datetime as dt
from random import randint
from ipywidgets import interact
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import Layout
from matplotlib import *

subscriptions = subm.load_subscriptions()
feedback_list = feedm.load_feedback()
def ValidateSUB():
    #Use this to check if the user is subscribed
    global ValidateUserSUB
    ValidateUserSUB = True
    if len(userID) != 4:
        print("Your userID can only be 4 characters long. Try again!")
    else:
        if subm.check_subscription(userID, subscriptions) == True: #"User", subscriptions in bracket
            print("Login successful! Welcome", userID)
        else:
            print("UserID \'{}\' wasn\'t recognised. Try again!".format(userID))
                
def ValidateRID(): #Maybe offer to show all record IDS? Could also do def ValidateRID(RecordID):
    global ValidatedRecID
    ValidatedRecID = False
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
                    return
        print("RecordID \'{}\' wasn\'t found. Try again!".format(RecordID))
        
def musicRent(): #Need to consider subscription limit of the user check by looping through rental.txt and see how many lines have that user ID
    userID = user_id_input.value
    recordID = record_id_input.value
    ValidateSUB()
    ValidateRID()
    if ValidateUserSUB == False or ValidatedRecID == False:
        return
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

def musicSearch():
    #y = False
    foundMatch = False
    f = open("Music_Info.txt", 'r').readlines()
    #while y == False:
    search = search_input.value.lower()
    for row in f:
        x = row.split(',')
        for i in range(6):
            if x[i-1].lower() == search.lower():
                foundMatch = True
                print("We found a record with:\n\nArtist Name: {}\nTitle: {}\nMedium: {}\nGenre: {}\n".format(x[1], x[2], x[3], x[4])) #Make more pretty
    if foundMatch == False:
        print("No matches were found in our database! ")

def musicReturn():
    userID = user_id_input.value
    recordID = record_id_input.value
    updatedRentals = []
    date = str(dt.datetime.now().date())
    ValidateRID(recordID)
    if ValidatedRecID == False:
        return
    f = open("Rental.txt", "r").readlines()
    for line in f:
        tempSearch = line.split(",") 
        if tempSearch[0] == recordID:
            if tempSearch[2].strip() == "":
                updatedRentals.append("{},{},{},{}\n".format(recordID,tempSearch[1],date,userID))
            else:
                print("This record isn\'t returnable!")
        else:
            updatedRentals.append(line)
    with open("Rental.txt", "w") as q:
        q.writelines(updatedRentals)
    #THESE SHOULD COME AT END
    StarRating = star_rating_input.value
    OptFeedback = feedback_input.value.strip() 
    #if feedback_input.value.strip() else "N/A"
    feedm.add_feedback(recordID, StarRating, OptFeedback, "Music_Feedback.txt")
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


user_id_input = widgets.Text(description="User ID:", layout=Layout(width='300px'))
record_id_input = widgets.Text(description="Record ID:", layout=Layout(width='300px'))
search_input = widgets.Text(description="Search:", layout=Layout(width='300px'))
star_rating_input = widgets.BoundedIntText(description="Rating (1-5):", min=1, max=5, layout=Layout(width='300px'))
feedback_input = widgets.Textarea(description="Feedback:", layout=Layout(width='300px'))
validate_sub_button = widgets.Button(description="Validate Subscription")
validate_rid_button = widgets.Button(description="Validate Record ID")
rent_button = widgets.Button(description="Rent Music")
search_button = widgets.Button(description="Search Music")
return_button = widgets.Button(description="Return Music")
prune_button = widgets.Button(description="Prune Inventory")

output = widgets.Output()

def on_validate_sub_button_clicked(b):
    with output:
        output.clear_output()
        ValidateSUB(user_id_input.value)

def on_validate_rid_button_clicked(b):
    with output:
        output.clear_output()
        ValidateRID(record_id_input.value)

def on_rent_button_clicked(b):
    with output:
        output.clear_output()
        musicRent()

def on_search_button_clicked(b):
    with output:
        output.clear_output()
        musicSearch()

def on_return_button_clicked(b):
    with output:
        output.clear_output()
        musicReturn()

def on_prune_button_clicked(b):
    with output:
        output.clear_output()
        invPrune()


validate_sub_button.on_click(on_validate_sub_button_clicked)
validate_rid_button.on_click(on_validate_rid_button_clicked)
rent_button.on_click(on_rent_button_clicked)
search_button.on_click(on_search_button_clicked)
return_button.on_click(on_return_button_clicked)
prune_button.on_click(on_prune_button_clicked)

# Display the widgets
widgets.VBox([
    user_id_input,
    validate_sub_button,
    record_id_input,
    validate_rid_button,
    rent_button,
    search_input,
    search_button,
    star_rating_input,
    feedback_input,
    return_button,
    prune_button,
    output
])
    
