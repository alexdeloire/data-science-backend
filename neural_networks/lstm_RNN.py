import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


dict_model_1 = {
    "column_name" : "quels enseignements vous semblent les plus utiles pour l'exercice de votre metier et votre insertion professionnelle ?",
    "tokenizer_path" : 'tokenizerPolyChatU.pkl',
    "model_path" : 'modelPolyChatU.keras',
    "label_encoder_path" : 'labelEncoderPolyChatU.pkl',
    "file_name" : 'formation_quels_enseignements_vous_semblent_les_plus_utiles_pour_lexercice_de_votre_metier_et_votre_insertion_professionnelle.csv'
}

dict_model_2 = {
    "column_name" : "parmi les enseignements fournis par l'ecole, quels sont ceux qui meriteraient d'etre approfondis ou renforces ?",
    "tokenizer_path" : 'tokenizerPolyChatR.pkl',
    "model_path" : 'modelPolyChatR.keras',
    "label_encoder_path" : 'labelEncoderPolyChatR.pkl',
    "file_name" : "formation_parmi_les_enseignements_fournis_par_lecole_quels_sont_ceux_qui_meriteraient_detre_approfondis_ou_renforces.csv"
}

dict_model_3 = {
    "column_name" : "quels enseignements, absents de votre formation, vous auraient ete utiles ?",
    "tokenizer_path" : 'tokenizerPolyChatA.pkl',
    "model_path" : 'modelPolyChatA.keras',
    "label_encoder_path" : 'labelEncoderPolyChatA.pkl',
    "file_name" : 'formation_quels_enseignements_absents_de_votre_formation_vous_auraient_ete_utiles.csv'
}

dict_model_4 = {
    "column_name" : "quels enseignements, presents dans votre formation, vous paraissent inutiles ?",
    "tokenizer_path" : 'tokenizerPolyChatI.pkl',
    "model_path" : 'modelPolyChatI.keras',
    "label_encoder_path" : 'labelEncoderPolyChatI.pkl',
    "file_name" : 'formation_quels_enseignements_presents_dans_votre_formation_vous_paraissent_inutiles.csv'
}


dict_list = [dict_model_1, dict_model_2, dict_model_3, dict_model_4]


for dict_model in dict_list:
    column_name = dict_model["column_name"]
    tokenizer_path = dict_model["tokenizer_path"]
    label_encoder_path = dict_model["label_encoder_path"]
    model_path = dict_model["model_path"]
    file_name = dict_model["file_name"]
    
    full_path = "../training_and_graph_data/" + file_name

    # Load data
    data = pd.read_csv(full_path)

    # Test if there are any NaN values in the column
    print(f"Number of NaN values in {column_name}: {data[column_name].isnull().sum()}")

    # Handle NaN values by filling them with an empty string
    data[column_name] = data[column_name].fillna("")

    # Tokenize and preprocess text data in French
    stop_words = set(stopwords.words("french"))
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(data[column_name].astype(str).apply(word_tokenize).apply(lambda x: [word for word in x if word.lower() not in stop_words]))
    sequences = tokenizer.texts_to_sequences(data[column_name])
    padded_sequences = pad_sequences(sequences)  

    # Save tokenizer
    #tokenizer_path = 'tokenizer.pkl'
    with open(tokenizer_path, 'wb') as f:
        pickle.dump(tokenizer, f, protocol=pickle.HIGHEST_PROTOCOL)

    # Label encoding for sectors
    label_encoder = LabelEncoder()
    data["SectorEncoded"] = label_encoder.fit_transform(data["formation"])

    # Save label encoder
    #label_encoder_path = 'label_encoder.pkl'
    with open(label_encoder_path, 'wb') as f:
        pickle.dump(label_encoder, f, protocol=pickle.HIGHEST_PROTOCOL)

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

    # Show model summary
    model.summary()

    # Train the model
    model.fit(X_train, y_train, epochs=1, batch_size=32, validation_split=0.2)

    # Save the model
    model.save(model_path)

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
