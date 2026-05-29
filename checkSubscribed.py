import subscriptionManager as subm
import feedbackManager as feedm

subscriptions = subm.load_subscriptions()
feedback_list = feedm.load_feedback()
#print(subscriptions)
def checkSubscribed():
    #Use this to check if the user is subscribed
    while True:
        userID = input("What is your unique customer ID: ")
        if len(userID) != 4:
            print("Your userID can only be 4 characters long. Try again!")
        else:
            if subm.check_subscription(userID, subscriptions) == True: #"User", subscriptions in bracket
                print("Login successful! Welcome", userID)
                break
            else:
                print("UserID \'{}\' wasn\'t recognised. Try again!".format(userID))
    
#checkSubscribed()
