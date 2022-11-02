# Import libraries.
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import random

# The file is written to be run on Colab with the drive mounted and the folders created along with the inputs stored
with open("/content/drive/My Drive/ISI-Project/processed_data.txt","rb") as f:
	all_data = pickle.load(f)

# Randomly shuffle the data
# all_data = all_data[0:100]
random.shuffle(all_data)

# Find the total length of the data
TotalLen = len(all_data)
# 90% of the total length is the Train set length
TrainLen = int(90*TotalLen/100)
# Remaining is the test set
TestLen = TotalLen - TrainLen

# Get the train and test set via splicing
TrainSet = all_data[0:TrainLen]
TestSet = all_data[TrainLen:]

# Train_poems is the set of all the poems only which will be used to train the model
train_poems = []

# Store the poems from the train set into it
for elem in TrainSet:
	train_poems.append(elem[4])

def identity_func(doc):
	return doc

# Start the working on btf
print("Start btf")
# Intialize the model
btf = TfidfVectorizer(binary=True,
	norm=None,
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
    min_df = 500,
	max_df = 0.8,
	token_pattern=None)
# Fit the model
btf.fit(train_poems)
# Find the vector for the poems in the train set and store them too.
TrainSetWithVector_btf = []
for elem in TrainSet:
	elem.append(btf.transform([elem[4]]).toarray()[0].tolist())
	TrainSetWithVector_btf.append(elem)

# Find the vector for the poems in the test set and store them too.
TestSetWithVector_btf = []
for elem in TestSet:
	elem.append(btf.transform([elem[4]]).toarray()[0].tolist())
	TestSetWithVector_btf.append(elem)

print(len(TestSetWithVector_btf))
print(len(TrainSetWithVector_btf))

# Store the output vectors as pickle dumps
with open("/content/drive/My Drive/ISI-Project/test_data_btf","wb") as f:
	pickle.dump(TestSetWithVector_btf,f)

with open("/content/drive/My Drive/ISI-Project/train_data_btf","wb") as f:
	pickle.dump(TrainSetWithVector_btf,f)

print("end btf")

print("Start bow")
# Intialize the model
bow = TfidfVectorizer(binary=False,
	norm=None,
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
  min_df = 500,
	max_df = 0.8,
	token_pattern=None)
# Fit the model
bow.fit(train_poems)
# Find the vector for the poems in the train set and store them too.
TrainSetWithVector_bow = []
for elem in TrainSet:
	elem[5] = (bow.transform([elem[4]]).toarray()[0].tolist())
	TrainSetWithVector_bow.append(elem)

# Find the vector for the poems in the test set and store them too.
TestSetWithVector_bow = []
for elem in TestSet:
	elem[5] = (bow.transform([elem[4]]).toarray()[0].tolist())
	TestSetWithVector_bow.append(elem)

print(len(TestSetWithVector_bow))
print(len(TrainSetWithVector_bow))

# Store the output vectors as pickle dumps
with open("/content/drive/My Drive/ISI-Project/test_data_bow","wb") as f:
	pickle.dump(TestSetWithVector_bow,f)

with open("/content/drive/My Drive/ISI-Project/train_data_bow","wb") as f:
	pickle.dump(TrainSetWithVector_bow,f)
print("end bow")

print("Start tfl1")
# Intialize the model
tfl1 = TfidfVectorizer(binary=False,
	norm='l1',
	use_idf=False,
	smooth_idf=False,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
  min_df = 500,
	max_df = 0.8,
	token_pattern=None)

# Fit the model
tfl1.fit(train_poems)
# Find the vector for the poems in the train set and store them too.
TrainSetWithVector_tfl1 = []
for elem in TrainSet:
	elem[5] = (tfl1.transform([elem[4]]).toarray()[0].tolist())
	TrainSetWithVector_tfl1.append(elem)

# Find the vector for the poems in the test set and store them too.
TestSetWithVector_tfl1 = []
for elem in TestSet:
	elem[5] = (tfl1.transform([elem[4]]).toarray()[0].tolist())
	TestSetWithVector_tfl1.append(elem)

print(len(TestSetWithVector_tfl1))
print(len(TrainSetWithVector_tfl1))

# Store the output vectors as pickle dumps
with open("/content/drive/My Drive/ISI-Project/test_data_tfl1","wb") as f:
	pickle.dump(TestSetWithVector_tfl1,f)

with open("/content/drive/My Drive/ISI-Project/train_data_tfl1","wb") as f:
	pickle.dump(TrainSetWithVector_tfl1,f)

print("end tfl1")

print("Start tfidf")
# Intialize the model
tfidf = TfidfVectorizer(binary=False,
	norm='l2',
	use_idf=True,
	smooth_idf=True,
	lowercase=False,
	tokenizer=identity_func,
	preprocessor=identity_func,
  min_df = 500,
	max_df = 0.8,
	token_pattern=None)

# Fit the model
tfidf.fit(train_poems)
# Find the vector for the poems in the train set and store them too.
TrainSetWithVector_tfidf = []
for elem in TrainSet:
	elem[5] = (tfidf.transform([elem[4]]).toarray()[0].tolist())
	TrainSetWithVector_tfidf.append(elem)

# Find the vector for the poems in the test set and store them too.
TestSetWithVector_tfidf = []
for elem in TestSet:
	elem[5] = (tfidf.transform([elem[4]]).toarray()[0].tolist())
	TestSetWithVector_tfidf.append(elem)

print(len(TestSetWithVector_tfidf))
print(len(TrainSetWithVector_tfidf))

# Store the output vectors as pickle dumps
with open("/content/drive/My Drive/ISI-Project/test_data_tfidf","wb") as f:
	pickle.dump(TestSetWithVector_tfidf,f)

with open("/content/drive/My Drive/ISI-Project/train_data_tfidf","wb") as f:
	pickle.dump(TrainSetWithVector_tfidf,f)
	
print("end tfidf")