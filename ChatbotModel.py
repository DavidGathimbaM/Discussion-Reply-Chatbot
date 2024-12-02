from transformers import AutoModelForCausalLM, AutoTokenizer

class ChatbotModel:
    def __init__(self):
        # Load GPT-2 model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.model = AutoModelForCausalLM.from_pretrained("gpt2")

    def generate_response(self, input_text, max_length=50):
        # Tokenize user input
        inputs = self.tokenizer.encode(input_text, return_tensors="pt")
        
        # Generate response
        outputs = self.model.generate(
            inputs, 
            max_length=max_length, 
            num_return_sequences=1, 
            no_repeat_ngram_size=2, 
            top_k=50, 
            top_p=0.95, 
            temperature=0.7
        )
        
        # Decode and return response
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
