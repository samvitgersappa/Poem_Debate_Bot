import tkinter as tk
from tkinter import scrolledtext
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import numpy as np

class PoemGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Poem Generator")

        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2", do_sample=True)
        self.model = GPT2LMHeadModel.from_pretrained("gpt2", do_sample=True)

        self.label = tk.Label(master, text="Enter a topic or keywords:")
        self.label.pack()

        self.topic_entry = tk.Entry(master)
        self.topic_entry.pack()

        self.poem_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.poem_text.pack()

        self.generate_button = tk.Button(master, text="Generate Poem", command=self.generate_poem)
        self.generate_button.pack()

    def generate_poem(self):
        topic = self.topic_entry.get()
        if topic:
            prompt = np.random.choice(additional_prompts) + f"{topic}"
            generated_poem = self.generate_poem_text(prompt)
            self.poem_text.delete(1.0, tk.END)
            self.poem_text.insert(tk.END, generated_poem)

    def generate_poem_text(self, prompt, max_length=200):
        input_text = prompt
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=1,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.8,
            top_k=50,
            top_p=0.95,
            repetition_penalty=1.2
        )
        generated_poem = self.tokenizer.decode(output[0], skip_special_tokens=True)
        lines = []
        line = ""
        for word in generated_poem.split():
            line += word + " "
            if len(line.split()) >= np.random.randint(5, 8):  # Generate random line length between 5 and 7 words
                lines.append(line.strip())
                line = ""
        if line:
            lines.append(line.strip())
        return "\n".join(lines) + "."  # Add punctuation at the end of each line

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

root = tk.Tk()
app = PoemGeneratorApp(root)
root.mainloop()
