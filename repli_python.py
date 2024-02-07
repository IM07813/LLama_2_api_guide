import replicate
import sys

def run_model(prompt, seed=None):
    # Define input parameters
    input_params = {
        "prompt": prompt,
        "system_prompt": "You are a helpful assistant.",
        "max_new_tokens": 128,
        "min_new_tokens": -1,
        "temperature": 0.75,
        "top_p": 0.9,
        "top_k": 50,
        "stop_sequences": "",
        "debug": False
    }
    
    # Include seed parameter if provided
    if seed is not None:
        input_params["seed"] = seed

    # Run the model
    for event in replicate.stream("meta/llama-2-70b-chat", input=input_params):
        print(str(event), end="")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py 'prompt' [seed]")
        sys.exit(1)
    
    prompt = sys.argv[1]
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
    run_model(prompt, seed)

