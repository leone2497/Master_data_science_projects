import re
from abc import ABC, abstractmethod  # ABC = Abstract Base Class to create abstract classes

file_path = r"/Users/mattiadetommaso/Desktop/Allpy_MattiaDeTommaso/divinaCommedia.txt"

# Abstract base class for frequency analysis
class BaseFrequencyAnalyzer(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    # Pass acts as a placeholder, abstract method to load text from the file
    @abstractmethod
    def load_text(self):
        pass

    # Pass acts as a placeholder, abstract method for optional text preprocessing
    @abstractmethod
    def preprocess(self, text):
        pass

    # Pass acts as a placeholder, abstract method to compute character frequencies
    @abstractmethod
    def compute_frequencies(self, text):
        pass

# Returns the six most frequent characters in the text. This method is not abstract,
# so it is already implemented in the base class and can be used directly by subclasses
# without redefining. It relies on abstract methods that must be implemented in the subclass:
# - load_text(): to load text from the file
# - preprocess(): to normalize/clean the text
# - compute_frequencies(): to calculate character frequencies
    def guess6(self):
        text = self.load_text()
        text = self.preprocess(text)
        frequency = self.compute_frequencies(text)
        # sort letters first by descending frequency (-item[1]), then alphabetically (item[0])
        sorted_values = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))
        # take the first 6 sorted elements
        top6_letters = sorted_values[:6]

        top6 = ""

        for letter, _ in top6_letters:  # loop over tuples (letter, frequency)
            top6 += letter  # add only the letter to the string

        # Obtain the 6 most frequent letters
        return top6


# Concrete class that implements the abstract methods
class SimpleFrequencyAnalyzer(BaseFrequencyAnalyzer):
    def __init__(self, file_path):
        super().__init__(file_path)  # call the constructor of the base class

    # Load text from the file
    def load_text(self):
        with open(self.file_path, "r", encoding="utf-8") as f:  # "r" means read mode, encoding="utf-8" ensures proper reading of accented and special characters without errors
            return f.read()

    # Remove special characters and normalize
    def preprocess(self, text):
        text = re.sub(r'[^a-z0-9àèìòùáéíóú\s]', '', text.lower())  # remove everything except letters, numbers, and spaces
        text = re.sub(r'\s+', ' ', text).strip()  # replace sequences of spaces with a single space
        return text

    # Compute frequencies of alphanumeric characters
    def compute_frequencies(self, text):
        frequencies = {}  # empty dictionary to count letters

        for letter in text:
            if letter.isalnum():  # consider both letters and numbers
                if letter in frequencies:
                    frequencies[letter] += 1  # increment if already present
                else:
                    frequencies[letter] = 1  # initialize if new
        # Return the dictionary of frequencies
        return frequencies

# Create an instance of SimpleFrequencyAnalyzer passing the file path to analyze
top6_frequent_letters = SimpleFrequencyAnalyzer(file_path)

# Call the guess6() method on the created object:
# the method performs the entire flow (read file, clean text,
# calculate frequencies) and returns the 6 most frequent characters
top6 = top6_frequent_letters.guess6()
print("The six most frequent characters are", top6)
