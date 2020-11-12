import torch
from models.lstm import LstmModel
# from models.placeholder import PlaceholderModel


# Process arguments


# Hand-specified
NUM_EPOCHS = 100
NUM_HIDDEN_UNITS = 128
NUM_ENCODER_LAYERS = 2
NUM_DECODER_LAYERS = 2
LEARNING_RATE = 0.01
DROPOUT = 0.1
BATCH_SIZE = 32
CHECKPOINT = None





# Build model

model = LstmModel()


# Load checkpoint (if any)

checkpoint = torch.load(CHECKPOINT)



# Train




# Save here?