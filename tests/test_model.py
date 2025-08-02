from ctransformers import AutoModelForCausalLM
import time

def test_llama_model():
    print("🚀 Testing Llama-2-7B-Chat Model...")
    print("=" * 50)
    
    # Model path
    model_path = "llama-2-7b-chat.ggmlv3.q4_0.bin"
    
    try:
        print("📥 Loading model...")
        start_time = time.time()
        
        # Load the model
        llm = AutoModelForCausalLM.from_pretrained(
            model_path,
            model_type="llama",
            gpu_layers=0,  # Set to 0 for CPU, increase for GPU
            max_new_tokens=512,
            temperature=0.7
        )
        
        load_time = time.time() - start_time
        print(f"✅ Model loaded successfully in {load_time:.2f} seconds!")
        
        # Test prompts
        test_prompts = [
            "Hello, how are you?",
            "What is 2 + 2?",
            "Explain what a medical chatbot is in one sentence."
        ]
        
        print("\n🧪 Running test prompts...")
        print("-" * 30)
        
        for i, prompt in enumerate(test_prompts, 1):
            print(f"\nTest {i}: {prompt}")
            print("Response:")
            
            start_time = time.time()
            response = llm(prompt)
            response_time = time.time() - start_time
            
            print(f"'{response.strip()}'")
            print(f"⏱️  Response time: {response_time:.2f} seconds")
        
        print("\n🎉 Model test completed successfully!")
        print("Your Llama-2-7B-Chat model is working correctly!")
        
    except Exception as e:
        print(f"❌ Error testing model: {str(e)}")
        print("Please check if the model file is in the correct location.")

if __name__ == "__main__":
    test_llama_model()