import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import numpy as np
import random
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class DebateBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Debate Bot")
        self.motion_label = tk.Label(master, text="Enter the motion:")
        self.motion_label.grid(row=0, column=0)
        self.motion_entry = tk.Entry(master)
        self.motion_entry.grid(row=0, column=1)

        self.stance_label = tk.Label(master, text="Are you for or against the motion? Type 'for' or 'against':")
        self.stance_label.grid(row=1, column=0)
        self.stance_entry = tk.Entry(master)
        self.stance_entry.grid(row=1, column=1)

        self.argument_label = tk.Label(master, text="Enter your argument:")
        self.argument_label.grid(row=2, column=0)
        self.argument_entry = tk.Entry(master)
        self.argument_entry.grid(row=2, column=1)
        
        self.response_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=10)
        self.response_text.grid(row=3, column=0, columnspan=2)

       
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_argument)
        self.submit_button.grid(row=4, column=0, columnspan=2)

       
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2", do_sample=True)
        self.model = GPT2LMHeadModel.from_pretrained("gpt2", do_sample=True)

       
        self.response_history = set()

    def preprocess_prompt(self, prompt, motion, stance):
        context = f"The motion is '{motion}'. {stance} argues that "
        return context + prompt

    def generate_response(self, prompt, max_length=200):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_length=max_length,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=random.uniform(0.7, 1.0),
            top_p=0.95,
            repetition_penalty=1.2
        )
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def submit_argument(self):
        motion = self.motion_entry.get()
        stance = self.stance_entry.get()
        user_argument = self.argument_entry.get()

        if motion.lower() == 'exit' or stance.lower() == 'exit':
            self.master.quit()

        prompt_for = self.preprocess_prompt(user_argument, motion, "for")
        prompt_against = self.preprocess_prompt(user_argument, motion, "against")

        response_for = self.generate_response(prompt_for)
        while response_for in self.response_history:
            response_for = self.generate_response(prompt_for)

        response_against = self.generate_response(prompt_against)
        while response_against in self.response_history:
            response_against = self.generate_response(prompt_against)

        self.response_text.insert(tk.END, "Debate Bot (For): " + response_for + "\n" + "\n")
        self.response_text.insert(tk.END, "Debate Bot (Against): " + response_against + "\n")
        self.response_text.insert(tk.END, "\n")

        self.response_history.add(response_for)
        self.response_history.add(response_against)

root = tk.Tk()
app = DebateBotApp(root)
root.mainloop()
