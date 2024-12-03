import pyrebase

firebaseConfig = {
    "apiKey" : "AIzaSyDqe5n_h7Aep6ThjhwTy_6GtyzB2vyPfiU",
    "authDomain" : "team7-e5280.firebaseapp.com",
    "databaseURL" : "https://team7-e5280-default-rtdb.firebaseio.com",
    "projectId" : "team7-e5280",
    "storageBucket" : "team7-e5280.firebasestorage.app",
    "messagingSenderId" : "92957058272",
    "appId" : "1:92957058272:web:838178bdf7a20672d95c85",
    "measurementId" : "G-V3XZ4LBLSN"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

data = {
    'temperature': 20,
    'turbidity': 15}
parentId = 'iot_data';
childId = 'device1'
db.child(parentId).child(childId).set(data)
# db.child(userId).update({'name': 'Han'})
get_data = db.child(parentId).child(childId).get()
result = get_data.val()
print(result)
