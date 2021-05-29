1. Copy emnist-bymerge-test.csv and emnist-bymerge-train.csv into the folder EMNIST-bymerge


2. Change the path (to this folder EMNIST_bymerge) appropriately in the train.py file:

train = pd.read_csv("/users/swathi/desktop/EMNIST_bymerge/emnist-bymerge-train.csv")
test = pd.read_csv("/users/swathi/desktop/EMNIST_bymerge/emnist-bymerge-test.csv")

#saving architecture
model_json = model.to_json()
with open("/Users/Swathi/Desktop/EMNIST_bymerge/model.json", "w") as json_file:
    json_file.write(model_json)

#saving weights
model.save_weights("/Users/Swathi/Desktop/EMNIST_bymerge/model.h5")
print("Saved model to disk")