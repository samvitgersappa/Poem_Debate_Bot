!pip install transformers

import tbb
import modin.pandas as pd
import intel_extension_for_pytorch as ipex
import torch
import torch.nn as nn
import torch.optim as optim
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import numpy as np
import nltk


nltk.download('punkt')

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model= ipex.optimize(model)

optimizer = optim.Adam(model.parameters(), lr=0.001)

df=pd.read_csv("mean.csv")
df=df.drop("word_id", "up_vote", "down_vote", "author")

def policy_gradient_update(optimizer, rewards, logits, actions):
    loss = -torch.log(logits[range(len(logits)), actions])
    loss = torch.mul(loss, rewards)  
    loss = torch.mean(loss)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()



def calculate(reference, generated):
    reference_tokens = [token.lower() for token in nltk.word_tokenize(reference)]
    generated_tokens = [token.lower() for token in nltk.word_tokenize(generated)]
    
    # Calculate BLEU score with 4-gram precision
    bleu_score = sentence_bleu([reference_tokens], generated_tokens, weights=(0.25, 0.25, 0.25, 0.25))
    
    return bleu_score

# reference_sentence = "The quick brown fox jumps over the lazy dog."
# generated_sentence = "A fast brown fox leaps over the tired dog."

# reward = calculate_bleu(reference_sentence, generated_sentence)
# print(f"BLEU Score: {reward}")


num_epochs=10
for epoch in range(num_epochs):
    for word, sentence_meaning in data:
       
        input_ids = tokenizer.encode(word, return_tensors="pt")
        target_ids = tokenizer.encode(mean, return_tensors="pt")

       
        outputs = model(input_ids, labels=target_ids)
        logits = outputs.logits
        print(outputs)
       
        rewards = calculate(word, generated_sentence)

       
        actions = torch.argmax(logits, dim=-1)

        
        policy_gradient_update(optimizer, rewards, logits, actions)
