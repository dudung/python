import sys

# check number of arguments
n = len(sys.argv)
if n < 2:
  print("Usage: py ml_class_bin_mix.py [n]")
  print()
  print("n\t 0 for Bing Chat")
  print("\t 1 for Chat GPT 3.5")
  print()
  sys.exit(0)
else:
  # 0 = Bing Chat, 1 = ChatGPT 3.5
  AI = int(sys.argv[1])


# show choice
if AI == 0:
  print("Using code from Bing Chat")
if AI == 1:
  print("Using code from Chat GPT 3.5")


# import modules
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

if AI == 1:
  from sklearn.metrics \
  import accuracy_score, classification_report, confusion_matrix


# read data from file
if AI == 0:
  # load data
  data = pd.read_excel("data_xyz.xlsx")

if AI == 1:
  # Load the dataset from the XLSX file
  # Replace with the actual path to your XLSX file
  xlsx_path = 'data_xyz.xlsx'
  df = pd.read_excel(
    xlsx_path,
    #header=None,
    names=['Feature1', 'Feature2', 'Label']
  )


# get features and labels
if AI == 0:
  # split data into features and labels
  X = data.iloc[:,0:2]
  y = data.iloc[:,2]

if AI == 1:
  # Split the data into features (X) and labels (y)
  X = df[['Feature1', 'Feature2']]
  y = df['Label']



# get training and testing sets
if AI == 0:
  # split data into training and testing sets
  pass
  
if AI == 1:
  # Split the data into training and testing sets
  pass
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# adjust features
if AI == 0:
  # scale features
  scaler = StandardScaler()
  X_train = scaler.fit_transform(X_train)
  X_test = scaler.transform(X_test)

if AI == 1:
  # Standardize the features (optional but often recommended)
  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)


# create model
if AI == 0:
  # create and fit classifier
  clf = LogisticRegression()
  clf.fit(X_train, y_train)

if AI == 1:
  # Initialize the Logistic Regression model
  model = LogisticRegression()

  # Train the model
  model.fit(X_train_scaled, y_train)

  # Make predictions on the test set
  y_pred = model.predict(X_test_scaled)


# evaluate model
if AI == 0:
  # evaluate classifier
  accuracy = clf.score(X_test, y_test)
  print("Accuracy:", accuracy)

if AI == 1:
  # Evaluate the model
  accuracy = accuracy_score(y_test, y_pred)
  conf_matrix = confusion_matrix(y_test, y_pred)
  classification_rep = classification_report(y_test, y_pred)

  # Print the evaluation metrics
  print(f'Accuracy: {accuracy:.2f}')
  print(f'Confusion Matrix:\n{conf_matrix}')
  print(f'Classification Report:\n{classification_rep}')

if AI == 0:
  print()