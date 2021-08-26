from pyrebase import pyrebase

# Firebase project configurations
firebaseConfig = {"apiKey": "AIzaSyDpAFD94fxrxAQs_fGve4QsXkW8pOf9StY",
                  "authDomain": "spambot-f9b9e.firebaseapp.com",
                  "databaseURL": "https://spambot-f9b9e-default-rtdb.firebaseio.com/",
                  "projectId": "spambot-f9b9e",
                  "storageBucket": "spambot-f9b9e.appspot.com",
                  "messagingSenderId": "394557756447",
                  "appId": "1:394557756447:web:46502e99d94470703a312a",
                  "measurementId": "G-BZVMH8LMGW"}

# Integrating python script with Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# Number Verification
def numbercheck(number):
    data = db.child("Scammer's Info").get()
    found = False

    for person in data:
        if person.val()['Number'] == int(number):
            info = person.val()['Name']
            found = True

    if found:
        return info
    else:
        return -1
