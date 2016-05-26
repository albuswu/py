from firebase import firebase
firebase = firebase.FirebaseApplication('https://capstoneip.firebaseio.com', None)
result = firebase.get('/users', None)
print result

new_ID = 'Raspberry Pi'

result = firebase.post('/users', new_ID)
print result
