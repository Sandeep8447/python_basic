import pickle
#import json

user_data = {
    'cardNumber': '6222021907005214015',
    'password': 'hello',
    'lock_flag': 0,
    'balance': 0,
    'cost': 0,

}

f = file('test.pkl', 'w')
#f = file('test.json', 'w')
pickle.dump(user_data, f)
#json.dump(dic1, f)
f.close()

f = file("test.pkl")

#f = file("test.json")
data = pickle.load(f)
#data = json.load(f)
f.close()
print data['cost']
