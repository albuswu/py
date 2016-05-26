from firebase import firebase
URL = 'https://capstoneip.firebaseio.com'
firebase = firebase.FirebaseApplication(URL, None)

ID = 'Raspberry Pi'

result = firebase.get(ID,None)
print result

result = firebase.post(ID,{'b':'a'})
print result
