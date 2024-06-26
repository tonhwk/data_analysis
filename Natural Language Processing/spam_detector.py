# spam_detector.py

import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score, roc_curve
import joblib
import matplotlib.pyplot as plt

# Download required NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the dataset
df = pd.read_csv('sms_spam.csv')

# Display columns and first few rows
print(df.columns)
print(df.head())

# Check for missing values
print("Checking for missing values...")
print(df.isnull().sum())

# Drop rows with missing messages
df = df.dropna(subset=['message'])

# Fill any remaining missing values in 'message' with empty string
df['message'] = df['message'].fillna('')

# Ensure there are both "ham" and "spam" messages in the dataset
if df['label'].nunique() < 2:
    raise ValueError("The dataset must contain both 'ham' and 'spam' messages for training.")

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    tokens = word_tokenize(text)  # Tokenize the text
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]  # Stemming
    return ' '.join(tokens)

# Apply preprocessing to the message column
df['cleaned_text'] = df['message'].apply(preprocess_text)

# Check for balance of classes
print(df['label'].value_counts())

# Extract features using TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=3000)
X = tfidf_vectorizer.fit_transform(df['cleaned_text']).toarray()
y = df['label'].apply(lambda x: 1 if x == 'spam' else 0)  # Convert labels to binary

# Check for balance after preprocessing
print(y.value_counts())

# Ensure that the data contains both classes after preprocessing
if y.nunique() < 2:
    raise ValueError("The preprocessed data must contain both 'ham' and 'spam' messages.")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Classification Report:\n', classification_report(y_test, y_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))

# Calculate the ROC-AUC score
roc_auc = roc_auc_score(y_test, y_pred)
print('ROC-AUC Score:', roc_auc)

# Plot the ROC curve
fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:, 1])
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='Logistic Regression (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()

# Save the model and the TF-IDF vectorizer
joblib.dump(model, 'spam_classifier_model.pkl')
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
