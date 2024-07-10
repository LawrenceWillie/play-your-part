# slide.py

import tkinter as tk

class CardSlider:
    def __init__(self, root, cards):
        self.root = root
        self.cards = cards
        self.index = 0
        
        # Create a frame for the card
        self.card_frame = tk.Frame(root)
        self.card_frame.pack(pady=20)
        
        # Display the first card
        self.card_label = tk.Label(self.card_frame, text=self.cards[self.index], font=("Helvetica", 24))
        self.card_label.pack()
        
        # Create a frame for the buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)
        
        # Previous button
        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_prev_card)
        self.prev_button.pack(side="left", padx=10)
        
        # Next button
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_card)
        self.next_button.pack(side="right", padx=10)

    def show_prev_card(self):
        """Show the previous card."""
        if self.index > 0:
            self.index -= 1
            self.card_label.config(text=self.cards[self.index])

    def show_next_card(self):
        """Show the next card."""
        if self.index < len(self.cards) - 1:
            self.index += 1
            self.card_label.config(text=self.cards[self.index])

def main():
    root = tk.Tk()
    root.title("Card Slider")
    
    # List of cards
    cards = ["Card 1", "Card 2", "Card 3", "Card 4", "Card 5"]
    
    # Create a CardSlider instance
    slider = CardSlider(root, cards)
    
    root.mainloop()

if __name__ == "__main__":
    main()
