import tkinter as tk
from tkinter import filedialog, Text, scrolledtext
import threading
import json
from ollama_vision_chat import OllamaVisionChat  # Importiere die Klasse aus der ollama_vision_chat.py

class OllamaVisionChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ollama Vision Chat")

        self.ollama_chat = OllamaVisionChat()

       
        self.frame = tk.Frame(master, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        
        self.prompt_label = tk.Label(self.frame, text="Prompt:")
        self.prompt_label.grid(row=0, column=0, sticky="w")

        self.prompt_text = Text(self.frame, height=2, wrap=tk.WORD)
        self.prompt_text.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        
        self.image_label = tk.Label(self.frame, text="Bildpfad:")
        self.image_label.grid(row=1, column=0, sticky="w")

        self.image_entry = tk.Entry(self.frame)
        self.image_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        
        self.browse_button = tk.Button(self.frame, text="Durchsuchen", command=self.browse_image)
        self.browse_button.grid(row=1, column=2, padx=5, pady=5)

       
        self.process_button = tk.Button(self.frame, text="Verarbeiten", command=self.process_image)
        self.process_button.grid(row=2, column=1, pady=10)

        
        self.results_frame = tk.LabelFrame(master, text="Antworten", padx=10, pady=10)
        self.results_frame.pack(fill=tk.BOTH, expand=True)

        
        self.results_text = scrolledtext.ScrolledText(self.results_frame, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        
        self.frame.columnconfigure(1, weight=1)

    def browse_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if filepath:
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, filepath)

    def process_image(self):
        image_path = self.image_entry.get()
        prompt = self.prompt_text.get("1.0", tk.END).strip()

        if not image_path or not prompt:
            return

        self.results_text.insert(tk.END, f"Verarbeite Bild: {image_path}\n")
        self.results_text.insert(tk.END, f"Prompt: {prompt}\n")

        n
        threading.Thread(target=self.run_ollama_chat, args=(image_path, prompt)).start()

    def run_ollama_chat(self, image_path, prompt):
        response = self.ollama_chat.chat_with_image(image_path, prompt)
        if response:
            result_file = self.ollama_chat.save_result(image_path.split("/")[-1], prompt, response)
            result_text = json.dumps(response['response'], indent=2, ensure_ascii=False)
            self.results_text.insert(tk.END, f"\nAntwort gespeichert unter: {result_file}\n")
            self.results_text.insert(tk.END, "-" * 50 + "\n")
            self.results_text.insert(tk.END, result_text + "\n")
            self.results_text.insert(tk.END, "-" * 50 + "\n")
            self.results_text.insert(tk.END, f"Bild wurde in den verarbeiteten Ordner verschoben\n")
        else:
            self.results_text.insert(tk.END, "Fehler bei der Kommunikation mit Ollama\n")

def main():
    root = tk.Tk()
    app = OllamaVisionChatGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
