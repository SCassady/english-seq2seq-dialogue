###English deep-learning chatbots

This project will include implementations of several dialogue systems. They are primarily designed for English, but may be expanded to work on some other languages.

The goal is a common interface to chat with bots using different algorithms, approaches. There will likely also be some experimentation with different datasets.

#####The potential systems:
- (In-progress) LSTM Seq2Seq (based on Vinyals et al; https://arxiv.org/pdf/1506.05869, as well as the pytorch tutorial; https://pytorch.org/tutorials/beginner/chatbot_tutorial.html)
- Transformer Seq2Seq (potentially based on https://arxiv.org/pdf/2001.09977)
- RL (li et al; https://arxiv.org/pdf/1606.01541)
- Adversarial generation (li et al; https://arxiv.org/pdf/1701.06547)
- Using a pre-trained LM (BERT or GPT)