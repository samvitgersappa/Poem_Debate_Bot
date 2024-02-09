import numpy as np
from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2", do_sample=True)
model = GPT2LMHeadModel.from_pretrained("gpt2", do_sample=True)

def process_user_input(user_input):
    return user_input

def generate_poem(model, tokenizer, topic, max_length=200):
    input_text = topic
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.8,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.2
    )

    generated_poem = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_poem

additional_prompts = [
    "A river flows silently through the forest,",
    "In the heart of the city, amidst the hustle and bustle,",
    "Underneath the starry night sky,",
    "Lost in the labyrinth of dreams,",
    "Amidst the ruins of an ancient civilization,",
    "On the edge of the world, where the sky meets the sea,",
    "In the quiet corner of a forgotten library,",
    "Within the depths of a forgotten memory,",
    "In the echoes of time, whispers can be heard,",
    "Beneath the facade of reality, lies a hidden truth,"
]

user_input = input("Enter a topic or keywords: ")
topic = process_user_input(user_input)
prompt = np.random.choice(additional_prompts) + f" A {topic} stands alone in the meadow,"
generated_poem = generate_poem(model, tokenizer, prompt)
print(generated_poem)
