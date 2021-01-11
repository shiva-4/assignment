import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import random

cred = credentials.Certificate("my-project.json")
firebase_admin.initialize_app(cred)
print("Working")

db = firestore.client()
doc_ref = db.collection("movies").document("Bollywood")

data = {"Name":["war","kgf","3-idiot","family-man","dangal"],
       "collection":[400,500,200,100,600]}
doc_ref.set(data)
print("done")

 
movie = database["Name"]
player = input("Write your Name: ")
print("Guess the character: ")
print("You have 10 chance to get the movie name: ")
print("Best of luck!",player)


count = 10

geuss= ""

word = random.choice(movie) #war

while count>0:
    fail = 0
    for char in word:
        if char in geuss:
            print(char)
        else:
            print("_")
            fail+=1
            
            
    if fail==0:
        print("Congratulation you won!!!")
        print("Movie Name was:",word)
        break
        
    g = input("Enter your character: ")
    geuss = geuss+g
    
    if g not in word:
        count = count-1
        print("Wrong Answer:(")

        print("You have ",count,"more geusses")








