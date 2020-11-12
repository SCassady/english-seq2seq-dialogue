import random
import torch
import torch.nn as nn


class LstmModel:

    def __init__(self, num_epochs, num_hidden_units, num_en_layers, num_de_layers, learning_rate, vocabulary, dropout=0):
        self.dialogueHistory = []
        self.num_epochs = num_epochs
        self.vocabulary = vocabulary


        # Create embedding
        self.embedding = nn.Embedding(vocabulary.num_words, num_hidden_units)

        # Build sub-components
        self.encoder = LstmEncoder(self.embedding, num_hidden_units, num_en_layers, dropout)
        self.decoder = LstmDecoder(self.embedding, num_hidden_units, num_de_layers, dropout)


    def train(self, epochs):
        self.epochs = epochs

        for i in range(epochs):
            self._train_pass()


    def _train_pass(self):
        pass

    def predict(self, input):
        return ""

    # def get_response(self, input):
    #     # Returns response
    #
    #     return self.predict(input)

class LstmEncoder(nn.Module):

    def __init__(self, embedding, hidden_size, num_layers, dropout=0):
        super(LstmEncoder, self).__init__()
        # self.input_size = input_size # Need this here?
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.dropout = dropout

        self.embedding = embedding  # embedding instance

        self.lstm = nn.LSTM(hidden_size,
                            hidden_size,
                            num_layers,
                            dropout=(0 if num_layers == 1 else dropout),
                            bidirectional=True)

    def forward(self, input_seq, input_lengths, hidden=None):
        # Forward operation

        # convert to embeddings
        embedded = self.embedding(input_seq)

        # pack
        packed = nn.utils.rnn.pack_padded_sequence(embedded, input_lengths)

        # forward pass
        outputs, hidden = self.lstm(packed, hidden)

        # unpack
        outputs, _ = nn.utils.rnn.pad_packed_sequence(outputs)

        # sum bidirectional outputs
        outputs = outputs[:, :, :self.hidden_size] + outputs[:, :, self.hidden_size:]

        return outputs, hidden


class Attention(nn.Module):

    def __init__(self):
        super(Attention, self).__init__()
        self.layer_count = 1

    def forward(self):
        # Forward operation

        return ""


class LstmDecoder(nn.Module):

    def __init__(self, embedding, hidden_size, num_layers, dropout=0):
        super(LstmDecoder, self).__init__()
        self.layer_count = 1

        self.attention = Attention()

    def forward(self):
        # Forward operation

        return ""



