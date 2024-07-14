# Customer Support- Finetuning GPT2 on Custom Dataset
![Screenshot 2024-07-14 141546](https://github.com/user-attachments/assets/c3f625f1-f810-42fd-a462-23da1d21f11f)

## Example
- [Example Image]()
## Description
- This repository contains a fine-tuned GPT-2 model designed to automate customer support interactions. 
- The model is capable of generating context-aware responses to common customer queries, enhancing customer engagement and reducing the workload on human support agents.

[Click here for the Model](https://drive.google.com/drive/folders/1_R2nEUAD0EdMzQVBS5APH0VgIb1jh6J7?usp=drive_link)

## Run the Model Online
- Install the required libraries
- Copy the code from Customer Support Text Generation Model.ipynb and run it on Google Colab ( recommended as GPU is required)
- Modify the generate_response() parameter to get the desired answer

## Run the Model Locally 
- Run the Customer Support Text Generation Model.ipynb on Gooogle Colab( recommended as GPU is required)
- After running the notebook a finetuned_gpt2 zipped folder will be downloaded to your local device. Unzip the folder
- Place the contents of the finetuned_gpt2 folder in your Python IDE(like Pycharm) in the root directory of your project 
- Install the neccessary libraries
- In main.py load the model and tokenizer by specifying the path to the finetuned_gpt2 folder
- Manipulate the generate_response() according to your needs to get the desired answers.
- Run the main.py file

## Finetune a Model on your Dataset
- Make sure the you have enough data to train the model
- You just need to  odify this line in the notebook:-
 Combine the columns into a single text field for training
df['input_text'] = df.apply(lambda row: f"Query: {row['Message']} Response: {row['Response']}", axis=1)
according to the columns in your dataset
- Run the notebook, modify the training arguments, outputs according to your needs
- Your model is ready
