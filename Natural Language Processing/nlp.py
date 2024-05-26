import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data = pd.read_csv('imdb_reviews.csv')

# Prepare the data
X = data['review']
y = data['sentiment'].apply(lambda x: 1 if x == 'positive' else 0)  # Convert sentiments to binary (1: positive, 0: negative)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predict sentiments on the test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=['negative', 'positive'])

print(f'Accuracy: {accuracy * 100:.2f}%')
print('Classification Report:')
print(report)

# Function to predict the sentiment of a new review
def predict_sentiment(review):
    review_tfidf = vectorizer.transform([review])  # Transform the input review to TF-IDF format
    prediction = model.predict(review_tfidf)  # Predict the sentiment
    sentiment = 'positive' if prediction[0] == 1 else 'negative'
    return sentiment

# Example usage
new_review = "The movie was absolutely horrendous with bad acting."
print(f'Review: {new_review}')
print(f'Sentiment: {predict_sentiment(new_review)}')
