import string
from tkinter import E


alphabet_letters = {"A":". __ ", "B":"__ ... ", "C":"__ . __ . ", "D":"__ .. ", "E":". ", 
"F":".. __ . " , "G":"__ __ . ", "H":".... ", "I":".. ", "J":". __ __ __ ", "K":"__ . __ ",
"L":". __ .. ", "M":"__ __ ", "N":"__ . ", "O":"__ __ __ ", "P":". __ __ . ", "Q":"__ __ . __ ",
"R":". __ . ", "S":"... ", "T":"__ ", "U":".. __ ", "V":"... __ ", "W":". __ __ ",
"X":"__ .. __ ", "Y":"__ . __ __ ", "Z":"__ __ .. ", "1":". __ __ __ __ ", 
"2":".. __ __ __ ", "3":"... __ __ ", "4":".... __ ", "5":"..... ", "6":"__ .... ",
"7":"__ __ ... ", "8":"__ __ __ .. ", "9":"__ __ __ __ . ", "0":"__ __ __ __ __ ", } 

letter_input = input("Enter your letter to translate into morse code: ").upper()
# print(letter_input)


class ConvertToMorse: 
    
    def __init__(self, letter_input, alphabet_letters):
        self.alphabet_letters=alphabet_letters
        self.letter_input=letter_input
        self.morse = ""
    
    # def __str__(self):
    #     return f'This is your morse code: {self.morse}'

    @property
    def string_to_morse_code(self):
        
        for letter in self.letter_input:
            for i in self.alphabet_letters:
                if letter == i: 
                    self.morse += alphabet_letters[letter]
            if letter == " ":
                self.morse += "    "
                if letter == ".":                
                    self.morse += "\n"
            # print(new_morse)
        return self.morse
        # print(self.morse)
    
    

morse_value = ConvertToMorse(letter_input,alphabet_letters,).string_to_morse_code
print(morse_value)