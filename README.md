# Customer Support- Finetuning GPT2 on Custom Dataset

## Example
![Screenshot 2024-07-14 141950](https://github.com/user-attachments/assets/e62c3c29-2fe5-40b7-8de2-8147bc8d32a2)

## TechStack/Fraemworks
- Finetuning GPT2
- Hugging Face Transformers

## Description
- This repository contains a fine-tuned GPT-2 model designed to automate customer support interactions. 
- The model is capable of generating context-aware responses to common customer queries, enhancing customer engagement and reducing the workload on human support agents.

[Click here for the Model](https://drive.google.com/drive/folders/1_R2nEUAD0EdMzQVBS5APH0VgIb1jh6J7?usp=drive_link)

## File Info
- Dataset - A cleaned modified version of a Kaggle dataset
- Notebook - A Google Colab Notebook
- Code - Main.py file of the Python Code run in Pycharm

## Run the Model Online
- Install the required libraries
- Copy the code from Customer Support Text Generation Model.ipynb and run it on Google Colab ( recommended as GPU is required)
- Modify the generate_response() parameter to get the desired answer

## Run the Model Locally 
- Run the Customer Support Text Generation Model.ipynb on Gooogle Colab( recommended as GPU is required)
- After running the notebook a finetuned_gpt2 zipped folder will be downloaded to your local device. Unzip the folder
- Alternatively you can download the Model from the link given above
- Place the contents of the finetuned_gpt2 folder in your Python IDE(like Pycharm) in the root directory of your project 
- Install the neccessary libraries
- In main.py load the model and tokenizer by specifying the path to the finetuned_gpt2 folder
- Manipulate the generate_response() according to your needs to get the desired answers.
- Run the main.py file

## Finetune a Model on your Dataset
- Make sure the you have enough data to train the model
- You just need to modify this line in the notebook :-
// Combine the columns into a single text field for training :
df['input_text'] = df.apply(lambda row: f"Query: {row['Message']} Response: {row['Response']}", axis=1) :
acoording to columns in your dataset
- Run the notebook, modify the training arguments, outputs according to your needs
- Your model is ready
