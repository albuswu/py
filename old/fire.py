from firebase import firebase
firebase = firebase.FirebaseApplication('https://capstoneip.firebaseio.com', None)
result = firebase.get('/Raspberry Pi', None)['-KHDNG57-4AOR_HXGXNW']
print result

IP = '1.1.1.1'

result = firebase.post('/Raspberry Pi', IP)
print result
