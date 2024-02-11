# Poem_Debate_Bot
This project contains two bots: a poem generator and a debate bot. The poem generator generates poems based on user input, while the debate bot engages in debates on various topics. The bots are made available on a tkinter based gui.

## Comparison with/without IPEX (Intel Extension for pytorch)

| No of Epochs       | Time Taken for training without IPEX     | Time Taken for training with IPEX     |
|--------------|-----------|------------|
| 10 | 0.408987      |    **0.1532082** |
| 20     | 0.66257214  |     **0.2639493** |
| 40     | 0.5762951  |     **0.3940904** |

## **How to use the poem bot**

**Step 1** : Run the poem_training_pytorch.ipynb notebook and save the **model_checkpoint.pth** file.
![1](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/ce3c135a-2c3e-4e4d-b5a4-d803898dd21e)



**Step 2** : Move the **model_checkpoints.pth** file to a seperate folder. Also put the poem_bot.py in the same folder and run it.

![2](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/001b9dcd-9def-44bd-a21d-a1ddaf25c67f)


## Societal Relevance

*The debate bot can help people improve their wordings, vocabulary and also introduce them to new perspectives related to the topic.*

*The poem generator is an attempt to help aspiring poets form phrases and generate topics that they can expand on*

## **The User Interface of the Debate Bot**
![Debate bot gui](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/ed52126f-7665-48b9-97e7-0cc3cef39ab4)

## **The Poem Generator**
![poem_bot](https://github.com/samvitgersappa/Poem_Debate_Bot/assets/124512060/7ab7950c-242f-4120-9494-b4f0ac095ce5)
