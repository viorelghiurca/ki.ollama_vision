import requests # type: ignore
import base64
from pathlib import Path
import time
import shutil
import json
from datetime import datetime

class OllamaVisionChat:
    def __init__(self, upload_folder="uploads", temperature=0.2):
        self.upload_folder = Path(upload_folder)
        self.processed_folder = Path("processed")
        self.results_folder = Path("results")
        self.temperature = temperature
        
        self.upload_folder.mkdir(exist_ok=True)
        self.processed_folder.mkdir(exist_ok=True)
        self.results_folder.mkdir(exist_ok=True)

    def encode_image_to_base64(self, image_path):
        """Encode image to base64"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def chat_with_image(self, image_path, prompt, model="llama3.2-vision"):
        """Send image to Ollama and get response"""
        base64_image = self.encode_image_to_base64(image_path)
        
        json_prompt = f"Please provide your response in JSON format. {prompt}"
        
        payload = {
            "model": model,
            "prompt": json_prompt,
            "images": [base64_image],
            "stream": False,
            "temperature": self.temperature,
            "format": "json"
        }

        try:
            response = requests.post("http://192.168.244.0:11434/api/generate", json=payload)
            response.raise_for_status()
            response_data = response.json()
            
            try:
                if isinstance(response_data['response'], str):
                    response_data['response'] = json.loads(response_data['response'])
            except json.JSONDecodeError:
                print("Warning: Model response was not valid JSON")
                
            return response_data
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Ollama: {e}")
            return None

    def save_result(self, image_name, prompt, response):
        """Save result as JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = self.results_folder / f"result_{image_name}_{timestamp}.json"
        
        result_data = {
            "timestamp": timestamp,
            "image_name": image_name,
            "prompt": prompt,
            "temperature": self.temperature,
            "response": response
        }
        
        with open(result_file, "w", encoding="utf-8") as f:
            json.dump(result_data, f, indent=2, ensure_ascii=False)
        
        return result_file

    def process_image(self, image_path):
        """Process a single image"""
        print(f"\nProcessing image: {image_path.name}")
        prompt = input("Enter your prompt for this image: ")
        
        print("Sending to Ollama...")
        response = self.chat_with_image(image_path, prompt)
        
        if response:
            result_file = self.save_result(image_path.name, prompt, response)
            
            print("\nResponse saved to:", result_file)
            print("\nResponse:")
            print("-" * 50)
            print(json.dumps(response['response'], indent=2))
            print("-" * 50)
            
            shutil.move(str(image_path), str(self.processed_folder / image_path.name))
            print(f"Image moved to processed folder")

    def process_upload_folder(self):
        """Process all images in upload folder"""
        image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
        
        while True:
            for file_path in self.upload_folder.iterdir():
                if file_path.suffix.lower() in image_extensions:
                    self.process_image(file_path)
            
            time.sleep(1)

def main():

    chat = OllamaVisionChat()
    
    print("\nWelcome to Ollama Vision Chat!")
    print(f"Upload folder: {chat.upload_folder.absolute()}")
    print(f"Processed folder: {chat.processed_folder.absolute()}")
    print(f"Results folder: {chat.results_folder.absolute()}")
    print(f"Temperature: {chat.temperature}")
    print("\nInstructions:")
    print("1. Copy your images to the 'uploads' folder")
    print("2. Enter prompts for each image when asked")
    print("3. Processed images will be moved to the 'processed' folder")
    print("4. Results will be saved as JSON in the 'results' folder")
    print("5. Press Ctrl+C to exit\n")
    
    try:
        chat.process_upload_folder()
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()