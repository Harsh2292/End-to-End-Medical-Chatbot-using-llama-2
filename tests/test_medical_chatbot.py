from ctransformers import AutoModelForCausalLM
import time

def create_medical_prompt(user_input):
    """Create a medical-focused prompt for the chatbot"""
    medical_instruction = """You are a helpful medical assistant. Provide accurate, helpful, and safe medical information. 
    Always remind users to consult healthcare professionals for serious medical concerns.
    
    User: {user_input}
    Assistant:"""
    
    return medical_instruction.format(user_input=user_input)

def test_medical_chatbot():
    print("🏥 Testing Medical Chatbot with Llama-2-7B-Chat...")
    print("=" * 60)
    
    # Model path
    model_path = "llama-2-7b-chat.ggmlv3.q4_0.bin"
    
    try:
        print("📥 Loading medical chatbot model...")
        start_time = time.time()
        
        # Load the model
        llm = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_type="llama",
            gpu_layers=0,  # Set to 0 for CPU, increase for GPU
            max_new_tokens=256,
            temperature=0.7
        )
        
        load_time = time.time() - start_time
        print(f"✅ Medical chatbot loaded in {load_time:.2f} seconds!")
        
        # Medical test queries
        medical_queries = [
            "What are the symptoms of a common cold?",
            "How can I lower my blood pressure naturally?",
            "What should I do if I have a fever?",
            "Explain the importance of regular exercise for health."
        ]
        
        print("\n🏥 Testing medical queries...")
        print("-" * 40)
        
        for i, query in enumerate(medical_queries, 1):
            print(f"\n🔍 Medical Query {i}: {query}")
            print("💬 Response:")
            
            # Create medical prompt
            prompt = create_medical_prompt(query)
            
            start_time = time.time()
            response = llm(prompt)
            response_time = time.time() - start_time
            
            # Clean up response
            response = response.strip()
            if "Assistant:" in response:
                response = response.split("Assistant:")[-1].strip()
            
            print(f"'{response}'")
            print(f"⏱️  Response time: {response_time:.2f} seconds")
            print("-" * 40)
        
        print("\n🎉 Medical chatbot test completed!")
        print("Your medical chatbot is ready for development!")
        
        # Interactive mode
        print("\n💬 Interactive Mode (type 'quit' to exit):")
        print("-" * 40)
        
        while True:
            user_input = input("\n👤 You: ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            if user_input:
                prompt = create_medical_prompt(user_input)
                response = llm(prompt)
                response = response.strip()
                if "Assistant:" in response:
                    response = response.split("Assistant:")[-1].strip()
                print(f"🤖 Assistant: {response}")
        
    except Exception as e:
        print(f"❌ Error testing medical chatbot: {str(e)}")
        print("Please check if the model file is in the correct location.")

if __name__ == "__main__":
    test_medical_chatbot()