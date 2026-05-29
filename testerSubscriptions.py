import subscriptionManager as subm
import feedbackManager as feedm

subscriptions = subm.load_subscriptions()
feedback_list = feedm.load_feedback()

print(subscriptions)
def checkSubscribed():
    #Use this to check if the user is subscribed
    subm.check_subscription() #"User", subscriptions in bracket
