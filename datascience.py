import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Load data
data = pd.read_csv("ETL/output_file.csv")
column_name = "quels enseignements vous semblent les plus utiles pour l'exercice de votre metier et votre insertion professionnelle ?"

# Handle NaN values by filling them with an empty string
data[column_name] = data[column_name].fillna("")

# Tokenize and preprocess text data in French
stop_words = set(stopwords.words("french"))
tokenizer = Tokenizer()
tokenizer.fit_on_texts(data[column_name].astype(str).apply(word_tokenize).apply(lambda x: [word for word in x if word.lower() not in stop_words]))
sequences = tokenizer.texts_to_sequences(data[column_name])
padded_sequences = pad_sequences(sequences)  # Specify maxlen

# Label encoding for sectors
label_encoder = LabelEncoder()
data["SectorEncoded"] = label_encoder.fit_transform(data["formation"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences, data["SectorEncoded"], test_size=0.2, random_state=42
)

# Build the model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32, input_length=padded_sequences.shape[1]))
model.add(LSTM(100))
model.add(Dense(10, activation="softmax"))

# Compile the model
model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train the model
model.fit(X_train, y_train, epochs=15, batch_size=32, validation_split=0.2)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_accuracy}")

# Make predictions
new_reviews = ["Management", "Programmation", "C++"]
new_sequences = tokenizer.texts_to_sequences(new_reviews)
new_padded_sequences = pad_sequences(new_sequences, maxlen=padded_sequences.shape[1])

predictions = model.predict(new_padded_sequences)
predicted_labels = label_encoder.inverse_transform([int(round(pred.argmax())) for pred in predictions])

print("Predicted Sectors:")
for review, predicted_label in zip(new_reviews, predicted_labels):
    print(f"Review: {review}, Predicted Sector: {predicted_label}")
