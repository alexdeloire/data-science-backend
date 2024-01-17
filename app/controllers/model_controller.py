from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np


def predict_sector(query, tokenizer, label_encoder, model):
    # Tokenize the query
    query_sequence = tokenizer.texts_to_sequences([query])
    padded_sequence = pad_sequences(
        query_sequence, maxlen=model.input_shape[1])

    # Make prediction
    prediction = model.predict(padded_sequence)

    # Get the predicted sector label
    predicted_index = np.argmax(prediction)

    # Map index to sector label using label encoder
    predicted_label = label_encoder.inverse_transform([predicted_index])[0]

    return predicted_label


if __name__ == "__main__":

   pass
