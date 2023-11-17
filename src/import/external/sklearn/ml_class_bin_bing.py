# import modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# load data
data = pd.read_excel("data_xyz.xlsx")

# split data into features and labels
X = data.iloc[:,0:2]
y = data.iloc[:,2]

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# create and fit classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# evaluate classifier
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
