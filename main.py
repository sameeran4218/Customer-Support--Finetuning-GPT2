from transformers import GPT2Tokenizer, GPT2LMHeadModel
import warnings
warnings.filterwarnings('ignore')

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained('finetuned_gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('finetuned_gpt2')

# Ensure pad_token is set to eos_token
tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.eos_token_id

def generate_response():
    # Tokenize input with padding and attention mask
    input_text=input('Enter your query')
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

    # Generate response with a high max_length
    outputs = model.generate(
        inputs['input_ids'],
        attention_mask=inputs['attention_mask'],  # Include attention mask
        max_length=500,  # Set to a high value to ensure complete responses
        num_return_sequences=1,
        temperature=0.5,  # Adjust temperature as needed
        top_k=50,  # Adjust top_k as needed
        top_p=0.95,  # Adjust top_p as needed
        no_repeat_ngram_size=2,  # Prevent repeating phrases
        early_stopping=True  # Stop early if end of sentence token is generated
    )

    # Decode and print the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response)

if __name__ == "__main__":
    while True:
        generate_response()
        cont=input("Enter y to continue and n to quit")
        if cont=='n':
            break


