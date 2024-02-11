# Poem_Debate_Bot

### Poem Generator

This project defines a GUI application using Tkinter for generating poems based on user-provided topics or keywords. It imports necessary libraries including tkinter, scrolledtext, and components from the transformers library such as GPT2Tokenizer and GPT2LMHeadModel. The app prompts the user to enter a topic, then generates a poem incorporating that topic using a pre-trained GPT-2 language model. The model is loaded, and upon clicking the "Generate Poem" button, it constructs a prompt using a random starter phrase from additional_prompts and the user's input topic. The generated poem is displayed in a scrollable text box. The poem generation involves setting parameters for temperature, top-k sampling, top-p sampling, and repetition penalty to control the creativity and coherence of the generated text.

### Debate bot


This code creates a Tkinter-based GUI application for a debate bot. Users input a debate motion, their stance ("for" or "against"), and their argument. Upon submission, the app generates responses from a GPT-2 language model based on the provided arguments. The responses are displayed in a scrollable text box. The app includes functionality to exit by typing 'exit' in either the motion or stance entry. The preprocess_prompt method formats the prompt with the motion and stance, while generate_response utilizes the GPT-2 model to generate responses. The app ensures response uniqueness by checking against a set of previous responses.

## Training 
The poem bot was trained on a file containing a 100000 line poem exposing it to most english words.

## File Contents

1) **Debate_bot_gui** - Run the code directly to interact with the debate bot.
2) **IPEX_pytorch_comparisons.ipynb** - Contains the code that we ran for comparing the training with/without IPEX
3) **Poem_training_pytorch.ipynb** - Trained the pytorch model
4) **poem.txt** - Poem dataset
5) **Poem_bot.py** - Run this code along with the model in the same folser to interact with the poem bot.

## Comparison with/without IPEX (Intel Extension for pytorch)

| No of Epochs       | Time Taken for training without IPEX     | Time Taken for training with IPEX     |
|--------------|-----------|------------|
| 10 | 0.408987      |    **0.1532082** |
| 20     | 0.66257214  |     **0.2639493** |
| 40     | 0.5762951  |     **0.3940904** |

## **How to use the poem bot**

**Step 1** : Run the poem_training_pytorch.ipynb notebook and save the **model_checkpoint.pth** file.
![Screenshot 2024-02-11 100442](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/acba02f7-5def-4f15-9948-a0374f29c786)




**Step 2** : Move the **model_checkpoints.pth** file to a seperate folder. Also put the poem_bot.py in the same folder and run it.

![2](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/001b9dcd-9def-44bd-a21d-a1ddaf25c67f)

*We used the pytorch version 1.13 as it was compatible with IPEX*


## Societal Relevance

*The debate bot can help people improve their wordings, vocabulary and also introduce them to new perspectives related to the topic.*

*The poem generator is an attempt to help aspiring poets form phrases and generate topics that they can expand on*

## **The User Interface of the Debate Bot**
![Debate bot gui](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/ed52126f-7665-48b9-97e7-0cc3cef39ab4)

## **The Poem Generator**
![poem_bot](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/7ab7950c-242f-4120-9494-b4f0ac095ce5)
