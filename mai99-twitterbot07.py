import tweepy
from tkinter import *

print ('Loading mai99-twitterbot07 program...')

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'
access_token_secret = 'xxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following " + user.name)

root = Tk()
root.title("mai99-twitterbot07")
root.geometry('200x400')

label1 = Label( root, text="Search").grid(column=0, row=1)
E1 = Entry(root, bd =5).grid(column=1, row=1)

label2 = Label( root, text="Number of Tweets").grid(column=0, row=2)
E2 = Entry(root, bd =5).grid(column=1, row=2)

label3 = Label( root, text="Response").grid(column=0, row=3)
E3 = Entry(root, bd =5).grid(column=1, row=3)

selected = IntVar()
E4 = Radiobutton(root, text="Reply", value="yes", variable=selected).grid(column=0, row=4)

label5 = Label( root, text="Retweet?").grid(column=0, row=5)
E5 = Entry(root, bd =5).grid(column=1, row=5)

label6 = Label( root, text="Favorite?").grid(column=0, row=6)
E6 = Entry(root, bd =5).grid(column=1, row=6)

label7 = Label( root, text="Follow?").grid(column=0, row=7)
E7 = Entry(root, bd =5).grid(column=1, row=7)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()

def getE4():
    return selected.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()

def mainFunction():
    getE1()
    search = getE1()
    
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    
    getE3()
    phrase = getE3()
    
    getE4()
    reply = IntVar()    
    
    getE5()
    retweet = getE5()
    
    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if retweet == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')   

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes": 
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')
                
            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break       
            
submit = Button(root, text ="Submit", command = mainFunction).grid(column=0, row=8)

#label1.pack()
#E1.pack()
#label2.pack()
#E2.pack()
#label3.pack()
#E3.pack()
#label5.pack()
#E5.pack()
#label6.pack()
#E6.pack()
#label7.pack()
#E7.pack()
#submit.pack(side =BOTTOM)

root.mainloop()