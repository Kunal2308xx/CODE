import tkinter as tk
import time
import random

# List of random paragraphs
paragraphs = [
    "The quick brown fox jumps over the lazy dog.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The early bird catches the worm.",
    "A picture is worth a thousand words.",
    "Actions speak louder than words."
]

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.paragraph = random.choice(paragraphs)
        self.start_time = None
        self.end_time = None

        self.paragraph_label = tk.Label(root, text=self.paragraph, wraplength=400, justify="left")
        self.paragraph_label.pack(pady=20)

        self.input_text = tk.Text(root, height=10, width=50, wrap='word')
        self.input_text.pack(pady=20)
        self.input_text.bind("<KeyRelease>", self.on_key_release)

        self.submit_button = tk.Button(root, text="Submit", command=self.on_submit)
        self.submit_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", fg="green")
        self.result_label.pack(pady=20)
        
        self.restart_button = tk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack(pady=10)
        
        self.input_text.focus_set()

    def on_key_release(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def on_submit(self):
        if self.start_time is not None:
            self.end_time = time.time()
            self.calculate_results()
            self.submit_button.config(state=tk.DISABLED)

    def calculate_results(self):
        total_time = self.end_time - self.start_time
        total_minutes = total_time / 60
        word_count = len(self.paragraph.split())
        words_per_minute = word_count / total_minutes

        typed_text = self.input_text.get("1.0", tk.END).strip()
        errors = self.calculate_errors(typed_text)

        self.result_label.config(text=f"WPM: {words_per_minute:.2f}, Errors: {errors}")

    def calculate_errors(self, typed_text):
        typed_words = typed_text.split()
        original_words = self.paragraph.split()
        
        errors = 0
        for i, word in enumerate(typed_words):
            if i < len(original_words) and word != original_words[i]:
                errors += 1
            elif i >= len(original_words):
                errors += 1

        return errors

    def restart(self):
        self.paragraph = random.choice(paragraphs)
        self.paragraph_label.config(text=self.paragraph)
        self.input_text.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None
        self.submit_button.config(state=tk.NORMAL)
        self.input_text.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
