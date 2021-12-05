from pyrebase import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyADVz0GVsrdmx5btazs3QFvoT-FJlJG1qM",
  "authDomain": "ranger-5738c.firebaseapp.com",
  "databaseURL": "https://ranger-5738c-default-rtdb.firebaseio.com/",
  "projectId": "ranger-5738c",
  "storageBucket": "ranger-5738c.appspot.com",
  "messagingSenderId": "981515063711",
  "appId": "1:981515063711:web:7322a758ceb9de9da7adaa",
  "measurementId": "G-787S5RXN90"
};



firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


data = [{"Name": "Suzanna Northcott", "Number": 7692886530},
{"Name": "Aggy Littell", "Number": 1579933899},
{"Name": "Norean Frascone", "Number": 5232233205},
{"Name": "Davie Troker", "Number": 4455715058},
{"Name": "Jamima Waldron", "Number": 6364236630},
{"Name": "Tedie Como", "Number": 3036351308},
{"Name": "Forrester Carlone", "Number": 8266394664},
{"Name": "Joannes Spira", "Number": 2305325456},
{"Name": "Calv Whitebread", "Number": 9347600891},
{"Name": "Jenny Davidovitz", "Number": 8978504549},
{"Name": "Barry McMurraya", "Number": 1177514855},
{"Name": "Teodora Hans", "Number": 2567397702},
{"Name": "Haskell Caddock", "Number": 3293715544},
{"Name": "Lek Beasleigh", "Number": 8607595921},
{"Name": "Mora Garret", "Number": 9609013145},
{"Name": "Johnathan Siccombe", "Number": 7893022667},
{"Name": "Leonore Barratt", "Number": 3276449112},
{"Name": "Mirelle Terry", "Number": 2501504104},
{"Name": "Bo Kleinsinger", "Number": 4137707646},
{"Name": "Lorne Sowrey", "Number": 1639928111},
{"Name": "Jade Tortoishell", "Number": 1066125520},
{"Name": "Lin Kester", "Number": 548282228},
{"Name": "Deina Swindle", "Number": 5324795330},
{"Name": "Ariela Glen", "Number": 3098203378},
{"Name": "Ange Chelam", "Number": 4374152352},
{"Name": "Laurie Algeo", "Number": 1231990184},
{"Name": "Rahal Scoon", "Number": 9914175952},
{"Name": "Krissy Akhurst", "Number": 1991676613},
{"Name": "Travers Charlon", "Number": 7705901121},
{"Name": "Bear Dods", "Number": 3102711641},
{"Name": "Ward McGilmartin", "Number": 1474808333},
{"Name": "Brianna Polson", "Number": 8368998763},
{"Name": "Kelly Redgrave", "Number": 1366464554},
{"Name": "Stormi Graveston", "Number": 4029848423},
{"Name": "Gerrard Ryley", "Number": 9236549133},
{"Name": "Marchelle Rockhill", "Number": 8092213745},
{"Name": "Brianne O'Lunny", "Number": 1436983836},
{"Name": "Lissy Kondrachenko", "Number": 8634883076},
{"Name": "Claudine MacDonell", "Number": 7463559270},
{"Name": "Wanda Deyes", "Number": 7935450592}]


for i in data:
    db.child("Scammer's Info").push(i)

print("Done")
