# Customer Support- Finetuning GPT2 on Custom Dataset

## Example
![Screenshot 2024-07-14 141950](https://github.com/user-attachments/assets/e62c3c29-2fe5-40b7-8de2-8147bc8d32a2)

![Screenshot 2024-07-15 103839](https://github.com/user-attachments/assets/4fb79bcf-ea81-4e7f-87e9-aeaac48f6fc8)

## TechStack/Frameworks
- Finetuning GPT2
- Hugging Face Transformers
- Flask

## Description
- This repository contains a fine-tuned GPT-2 model designed to automate customer support interactions. 
- The model is capable of generating context-aware responses to common customer queries, enhancing customer engagement and reducing the workload on human support agents.

## Model
[Click here for the Model](https://drive.google.com/drive/folders/1_R2nEUAD0EdMzQVBS5APH0VgIb1jh6J7?usp=drive_link)

## File Info
- Dataset - A cleaned modified version of a Kaggle dataset
- Notebook - A Google Colab Notebook
- Code
  1. Main.py file of the Python Code.
  2. app.py file of Flask Web app
  3. Templates/index.html contains html and javascript code of the webapp
  4. static/css contains the corresponding html webpage
- Model - finetuned_gpt2 folder contains the model files. Google Drive link is given above

## Run the Model 
- Copy the code from Customer Support Text Generation Model.ipynb and run it on Google Colab ( recommended as GPU is required)
- Modify the generate_response() parameter to get the desired answer
- Download the Model from the link given above
- Place the contents of the finetuned_gpt2 folder in your Python IDE(like Pycharm) in the root directory of your project 
- In main.py load the model and tokenizer by specifying the path to the finetuned_gpt2 folder
- Manipulate the generate_response() according to your needs to get the desired answers.
- You can also download a zip file of all the code, extract it and run python app.py then use the model on localhost:5000

## Finetune a Model on your Dataset
- Make sure the you have enough data to train the model
- You just need to modify this line in the notebook :-
-- // Combine the columns into a single text field for training :
-- df['input_text'] = df.apply(lambda row: f"Query: {row['Message']} Response: {row['Response']}", axis=1) : according to columns in your dataset
- Run the notebook, modify the training arguments, outputs according to your needs
- Your model is ready
