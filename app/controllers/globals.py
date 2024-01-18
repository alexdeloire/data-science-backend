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

# Specify paths to the saved tokenizers, encoders and model

modelPolyChatA_path = 'neural_networks/modelPolyChatA.keras'
modelPolyChatI_path = 'neural_networks/modelPolyChatI.keras'
modelPolyChatR_path = 'neural_networks/modelPolyChatR.keras'
modelPolyChatU_path = 'neural_networks/modelPolyChatU.keras'

tokenizerPolyChatA_path = 'neural_networks/tokenizerPolyChatA.pkl'
tokenizerPolyChatI_path = 'neural_networks/tokenizerPolyChatI.pkl'
tokenizerPolyChatR_path = 'neural_networks/tokenizerPolyChatR.pkl'
tokenizerPolyChatU_path = 'neural_networks/tokenizerPolyChatU.pkl'

encoderPolyChatA_path = 'neural_networks/labelEncoderPolyChatA.pkl'
encoderPolyChatI_path = 'neural_networks/labelEncoderPolyChatI.pkl'
encoderPolyChatR_path = 'neural_networks/labelEncoderPolyChatR.pkl'
encoderPolyChatU_path = 'neural_networks/labelEncoderPolyChatU.pkl'


# Load the global variables for the PolyChat models
# tokenizerPolyChatA, encoderPolyChatA, modelPolyChatA = load_tokenizer_and_encoder_and_model(tokenizerPolyChatA_path, encoderPolyChatA_path, modelPolyChatA_path)
# tokenizerPolyChatI, encoderPolyChatI, modelPolyChatI = load_tokenizer_and_encoder_and_model(tokenizerPolyChatI_path, encoderPolyChatI_path, modelPolyChatI_path)
# tokenizerPolyChatR, encoderPolyChatR, modelPolyChatR = load_tokenizer_and_encoder_and_model(tokenizerPolyChatR_path, encoderPolyChatR_path, modelPolyChatR_path)
# tokenizerPolyChatU, encoderPolyChatU, modelPolyChatU = load_tokenizer_and_encoder_and_model(tokenizerPolyChatU_path, encoderPolyChatU_path, modelPolyChatU_path)


# Load the global variables for the PolyChat models
tokenizerPolyChatA, encoderPolyChatA, modelPolyChatA = None, None, None
tokenizerPolyChatI, encoderPolyChatI, modelPolyChatI = None, None, None
tokenizerPolyChatR, encoderPolyChatR, modelPolyChatR = None, None, None
tokenizerPolyChatU, encoderPolyChatU, modelPolyChatU = None, None, None



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