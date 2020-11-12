from models.placeholder import PlaceholderModel
from models.lstm import  LstmModel
import sys


# ---- Preparation ----

# Process args
args = sys.argv
model_type = str(args[1]).lower()

# Build model
dialogueModel = None # Remove?
if model_type == "lstm":
    dialogueModel = LstmModel()
else:
    dialogueModel = PlaceholderModel()

# Load checkpoint
if  len(args) > 2:
    checkpoint_path = str(args[2]).lower()

    # Pass checkpoint to dialogue model


# ---- Chat logic ----

def get_response(text_in):
    # Call the chat-bot model here
    return dialogueModel.predict(text_in)


chat_turn = 0

print("------------- Chat starting! ---------------")
print("(Type 'quit' to exit.)\n")

while True:
    # Query user for input.
    user_input = input("YOU: ")
    print("")

    # Check for quit command.
    if user_input == "quit":
        print("Quitting...")
        sys.exit(0)

    # Receive, display response
    response = get_response(input)

    print_string = "MR. E: " + response
    print(print_string + "\n")

    chat_turn += 1