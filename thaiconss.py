import tkinter as tk
import random

# Thai consonants and their pronunciation with names
thai_consonants = {
    "ก": ("k/g", "gor kai"),
    "ข": ("kh", "khor khai"),
    "ค": ("kh", "khor khwai"),
    "ฆ": ("kh", "khor ra-khang"),
    "ง": ("ng", "ngor ngu"),
    "จ": ("ch", "jor jan"),
    "ฉ": ("ch", "chor ching"),
    "ช": ("ch", "chor chang"),
    "ซ": ("s", "sor so"),
    "ฌ": ("ch", "chor chaang"),
    "ญ": ("y", "yor ying"),
    "ฎ": ("d", "dor cha-da"),
    "ฏ": ("t", "tor pa-tak"),
    "ฐ": ("th", "thor than"),
    "ฑ": ("th/d", "thor mon-tho"),
    "ฒ": ("th", "thor phu-thao"),
    "ณ": ("n", "nor nen"),
    "ด": ("d", "dor dek"),
    "ต": ("t", "tor tao"),
    "ถ": ("th", "thor thung"),
    "ท": ("th", "thor thahan"),
    "ธ": ("th", "thor thong"),
    "น": ("n", "nor nu"),
    "บ": ("b", "bor baimai"),
    "ป": ("p", "por pla"),
    "ผ": ("ph", "phor phueng"),
    "ฝ": ("f", "for fa"),
    "พ": ("ph", "phor phan"),
    "ฟ": ("f", "for fan"),
    "ภ": ("ph", "phor sam-phao"),
    "ม": ("m", "mor ma"),
    "ย": ("y", "yor yak"),
    "ร": ("r", "ror ruea"),
    "ล": ("l", "lor ling"),
    "ว": ("w", "wor waen"),
    "ศ": ("s", "sor sala"),
    "ษ": ("s", "sor rue-si"),
    "ส": ("s", "sor suea"),
    "ห": ("h", "hor hip"),
    "ฬ": ("l", "lor chu-la"),
    "อ": ("o", "or ang"),
    "ฮ": ("h", "hor nok-huk")
}

class ThaiFlashcardGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcard Game")
        self.current_consonant = ""
        
        self.label = tk.Label(root, text="Press 'Next' to start", font=("Arial", 50))
        self.label.pack(pady=50)
        
        self.answer_label = tk.Label(root, text="", font=("Arial", 30), fg="blue")
        self.answer_label.pack(pady=20)
        
        self.name_label = tk.Label(root, text="", font=("Arial", 30), fg="green")
        self.name_label.pack(pady=20)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_card, font=("Arial", 20))
        self.next_button.pack(pady=10)
        
        self.show_button = tk.Button(root, text="Show Answer", command=self.show_answer, font=("Arial", 20))
        self.show_button.pack(pady=10)

    def next_card(self):
        self.current_consonant = random.choice(list(thai_consonants.keys()))
        self.label.config(text=self.current_consonant)
        self.answer_label.config(text="")
        self.name_label.config(text="")
    
    def show_answer(self):
        if self.current_consonant:
            pronunciation, name = thai_consonants[self.current_consonant]
            self.answer_label.config(text=pronunciation)
            self.name_label.config(text=name)

if __name__ == "__main__":
    root = tk.Tk()
    game = ThaiFlashcardGame(root)
    root.mainloop()