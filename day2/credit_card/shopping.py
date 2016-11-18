import pickle

your_data = {'foo': 'bar'}

# Store data (serialize)
with open('filename.pickle', 'wb') as handle:
    pickle.dump(your_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Load data (deserialize)
with open('filename.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

print(your_data == unserialized_data)