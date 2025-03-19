import os
import pandas as pd
import numpy as np
import random

class Book:
    """
    Represents a book with format, genre, and whitespace properties.
    """
    def __init__(self, genre: str, format_type: str, whitespace_percentage: float, page_area: int):
        self.genre = genre
        self.format_type = format_type
        self.whitespace_percentage = whitespace_percentage
        self.page_area = page_area
        self.whitespace_cm2 = self.calculate_whitespace()

    def calculate_whitespace(self) -> float:
        """Calculates the whitespace area in cm²."""
        return (self.whitespace_percentage / 100) * self.page_area

class BookDatasetGenerator:
    """
    Generates a dataset of books following the conditions of Simpson's Paradox.
    """
    SMALL_PAGE_AREA = 200  # in cm²
    LARGE_PAGE_AREA = 620  # in cm²
    LYRIC_WHITESPACE_MEAN = 33  # in %
    PROSE_WHITESPACE_MEAN = 19  # in %
    STD_DEV = 5  # Standard deviation for randomness
    NUM_BOOKS = 1000

    def __init__(self):
        self.books = []
        self.generate_books()

    def generate_books(self) -> None:
        """Generates books ensuring the paradox conditions are met."""
        for _ in range(self.NUM_BOOKS):
            genre = self.choose_genre()
            format_type = self.choose_format(genre)
            whitespace_percentage = self.generate_whitespace(genre)
            page_area = self.SMALL_PAGE_AREA if format_type == "Small" else self.LARGE_PAGE_AREA
            self.books.append(Book(genre, format_type, whitespace_percentage, page_area))

    def choose_genre(self) -> str:
        """Chooses a genre, ensuring more lyric books are in small format."""
        return random.choices(["Lyric", "Prose"], weights=[0.5, 0.5])[0]

    def choose_format(self, genre: str) -> str:
        """Chooses a format based on genre, ensuring correct distribution."""
        if genre == "Lyric":
            return random.choices(["Small", "Large"], weights=[0.85, 0.15])[0]
        else:
            return random.choices(["Small", "Large"], weights=[0.25, 0.75])[0]

    def generate_whitespace(self, genre: str) -> float:
        """Generates a normally distributed whitespace percentage."""
        mean = self.LYRIC_WHITESPACE_MEAN if genre == "Lyric" else self.PROSE_WHITESPACE_MEAN
        return max(0, min(100, np.random.normal(mean, self.STD_DEV)))

    def save_to_csv(self, file_path: str) -> None:
        """Saves the generated dataset to a CSV file."""
        df = pd.DataFrame([vars(book) for book in self.books])
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)

if __name__ == "__main__":
    dataset_generator = BookDatasetGenerator()
    dataset_generator.save_to_csv("./data/margin.csv")
    print("Dataset saved to ./data/margin.csv")

    # Load the dataset for statistical summary
    df = pd.read_csv("./data/margin.csv")
    
    # Compute averages
    avg_whitespace_by_genre = df.groupby("genre")["whitespace_cm2"].mean()
    avg_whitespace_by_format = df.groupby("format_type")["whitespace_cm2"].mean()
    avg_whitespace_total = df["whitespace_cm2"].mean()
    avg_whitespace_by_genre_format = df.groupby(["genre", "format_type"])["whitespace_cm2"].agg(["count", "mean"])
    
    print("\nStatistical Summary:")
    print("Average whitespace by genre:")
    print(avg_whitespace_by_genre)
    print("\nAverage whitespace by format:")
    print(avg_whitespace_by_format)
    print(f"\nOverall average whitespace: {avg_whitespace_total:.2f} cm²")
    print("\nAverage whitespace by genre and format:")
    print(avg_whitespace_by_genre_format)