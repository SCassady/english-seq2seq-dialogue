import random



class PlaceholderModel:

    def __init__(self):
        self.simpleResponses = [
            "Is that right?",
            "Sure...",
            "Not sure about that.",
            "I love that!",
            "Absolutely.",
            "How does that make you feel?",
            "I can totally relate to that.",
            "An interesting thought.",
            "Would you ever reconsider that?",
            "Ok, but how are you?"
        ]

        self.dialogueHistory = []


    def predict(self, input):
        # Returns random hand-written response.

        random.shuffle(self.simpleResponses)
        response = self.simpleResponses[random.randint(0, len(self.simpleResponses))]

        self.dialogueHistory.append(input)
        self.dialogueHistory.append(response)

        return response