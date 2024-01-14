import pickle
from tensorflow.keras.models import load_model

def load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, model_path):
    # Load tokenizer
    with open(tokenizer_path, 'rb') as f:
        tokenizer = pickle.load(f)
        
    with open(encoder_path, 'rb') as f:
        encoder = pickle.load(f)

    # Load model
    model = load_model(model_path)

    return tokenizer, encoder, model

# Specify paths to the saved tokenizer and model
tokenizer_path = 'neural_networks/tokenizer.pkl'
encoder_path = 'neural_networks/label_encoder.pkl'
model_path = 'neural_networks/model.keras'

# Load the global variables
loaded_tokenizer, loaded_encoder, loaded_model = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, model_path)


# Getters for the global variables
def get_tokenizer():
    return loaded_tokenizer

def get_encoder():
    return loaded_encoder

def get_model():
    return loaded_model
