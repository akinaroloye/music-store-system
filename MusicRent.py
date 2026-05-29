import checkSubscribed as CSub
import ValidateRID as VRID
import datetime as dt
def musicRent():
    date = str(dt.datetime.now().date())
    dateAdj = date.split("-")
    year, month, day = dateAdj[0], dateAdj[1], dateAdj[2]
    f = open("Rental.txt", "r").readlines()
    print(Validated)
    #RentRecord = input("Would you like to rent the record [y/n]: ")
    CSub.checkSubscribed()
    VRID.ValidateRID()
    #Need functionality to check its available
    #Return date would be blank if the record still hasnt been returned
    #Rental Date would be blank if a book hasnt ever been rented yet
    #When you rent a book perhaps replace rental date with datetime.now
    #And replace return date with null until the customer choses to return the item
    #WILL HAVE TO SWAP THE FILE IN VALIDATE RID TO RENTAL.TXT [EASY]
musicRent()
