import checkSubscribed as CSub
import datetime as dt
#CSub.checkSubscribed()
#dateNow = str(dt.datetime.now().date())
#print(date)
def ValidateRID():
    while True:
        Validated = False
        RecordID = input("Enter the record\'s unique 5-Character ID: ")
        if len(RecordID) != 5:
            print("Your RecordID can must be 5 characters long. Try again!")
        else:
            f = open("Music_info.txt", "r").readlines()
            while True:
                for line in f:
                    line = line.split(",")
                    if line[0] == RecordID:
                        print("RecordID found")
                        Validated = True
                        break
                break
            if Validated == False:
                print("RecordID \'{}\' wasn\'t found. Try again!".format(RecordID))
            else:
                break
           
#Check user subscription limit
#Could use driving countdown to compare date in subscription_info to current date
#ValidateRID()
