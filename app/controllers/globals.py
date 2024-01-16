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

modelPolyChatA_path = 'neural_networks/modelPolyChatA.keras'
modelPolyChatI_path = 'neural_networks/modelPolyChatI.keras'
modelPolyChatR_path = 'neural_networks/modelPolyChatR.keras'
modelPolyChatU_path = 'neural_networks/modelPolyChatU.keras'

# Load the global variables
loaded_tokenizer, loaded_encoder, loaded_model = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, model_path)

# Load the global variables for the PolyChat models
tokenizerPolyChatA, encoderPolyChatA, modelPolyChatA = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, modelPolyChatA_path)
tokenizerPolyChatI, encoderPolyChatI, modelPolyChatI = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, modelPolyChatI_path)
tokenizerPolyChatR, encoderPolyChatR, modelPolyChatR = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, modelPolyChatR_path)
tokenizerPolyChatU, encoderPolyChatU, modelPolyChatU = load_tokenizer_and_encoder_and_model(tokenizer_path, encoder_path, modelPolyChatU_path)

# Getters for the global variables
def get_tokenizer():
    return loaded_tokenizer

def get_encoder():
    return loaded_encoder

def get_model():
    return loaded_model


# Getters for the PolyChat models
def get_tokenizerPolyChatA():
    return tokenizerPolyChatA

def get_encoderPolyChatA():
    return encoderPolyChatA

def get_modelPolyChatA():
    return modelPolyChatA

def get_tokenizerPolyChatI():
    return tokenizerPolyChatI

def get_encoderPolyChatI():
    return encoderPolyChatI

def get_modelPolyChatI():
    return modelPolyChatI

def get_tokenizerPolyChatR():
    return tokenizerPolyChatR

def get_encoderPolyChatR():
    return encoderPolyChatR

def get_modelPolyChatR():
    return modelPolyChatR

def get_tokenizerPolyChatU():
    return tokenizerPolyChatU

def get_encoderPolyChatU():
    return encoderPolyChatU

def get_modelPolyChatU():
    return modelPolyChatU