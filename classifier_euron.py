# import libraries
import os
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from collections import Counter



def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir, f) for f in os.listdir(train_dir)]
    all_words = []
    for email in emails:
        dirs = [os.path.join(email, f) for f in os.listdir(email)]
        for d in dirs:
            emails = [os.path.join(d, f) for f in os.listdir(d)]
            for mail in emails:
                with open(mail, errors="ignore") as m:
                    for i, line in enumerate(m):
                        if i == 2:
                            words = line.split()
                            all_words += words

    dictionary = Counter(all_words)
    # Code for non-word removal
    list_to_remove = list(dictionary.keys())
    for item in list_to_remove:
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    return dictionary


def extract_features(mail_dir):
    files = [os.path.join(mail_dir, f) for f in os.listdir(mail_dir)]
    docID = 0;
    features_matrix = np.zeros((33713, 3000))
    train_labels = np.zeros(33713)
    for file in files:
        dirs = [os.path.join(file, f) for f in os.listdir(file)]
        for d in dirs:
            emails = [os.path.join(d, f) for f in os.listdir(d)]
            for mail in emails:
                with open(mail, errors="ignore") as m:
                    all_words = []
                    for line in m:
                        words = line.split()
                        all_words += words
                    for word in all_words:
                        wordID = 0
                        for i, d in enumerate(dictionary):
                            if d[0] == word:
                                wordID = i
                                features_matrix[docID, wordID] = all_words.count(word)
                train_labels[docID] = int(mail.split(".")[-2] == 'spam')
                docID = docID + 1

    return features_matrix, train_labels


train_dir = 'enron-spam'
dictionary = make_Dictionary(train_dir)

features, labels = extract_features(train_dir)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.40)
model0 = LinearSVC()
model0.fit(X_train, y_train)
result0 = model0.predict(X_test)

print(confusion_matrix(y_test, result0))
print("Linear SVC is: ", accuracy_score(y_test, result0))
# save the Linear SVC model in a .sav file
saveFile = "emailClassifier.enron.sav"
with open(saveFile,'wb') as file:
    pickle.dump(model0,file)
