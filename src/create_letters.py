import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

from datetime import datetime, timedelta

class LetterSimulation:
    def __init__(self, lambda_value=3, start_date="1909-01-01", end_date="1912-03-31", seed=None):
        """
        Simuliert die Anzahl der Briefe pro Tag über einen historischen Zeitraum.
        :param lambda_value: Durchschnittliche Anzahl der Briefe pro Tag (Poisson-Parameter)
        :param start_date: Startdatum der Simulation (Format: YYYY-MM-DD)
        :param end_date: Enddatum der Simulation (Format: YYYY-MM-DD)
        :param seed: Zufallsseed für reproduzierbare Ergebnisse
        """
        self.lambda_value = lambda_value
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.seed = seed
        self.data = None
        self.dates = self._generate_dates()

    def _generate_dates(self):
        """Erzeugt eine Liste mit allen Tagen zwischen Start- und Enddatum."""
        num_days = (self.end_date - self.start_date).days + 1
        return [self.start_date + timedelta(days=i) for i in range(num_days)]

    def generate_data(self):
        """Generiert Poisson-verteilte Briefanzahlen pro Tag für den Zeitraum."""
        if self.seed is not None:
            np.random.seed(self.seed)
        self.data = np.random.poisson(self.lambda_value, len(self.dates))

    def save_to_csv(self, filename="letters.csv"):
        """Speichert die generierten Daten als CSV mit Datumsspalte."""
        df = pd.DataFrame({"Date": self.dates, "Letters": self.data})
        df.to_csv(filename, index=False, date_format="%Y-%m-%d")
        print(f"Daten wurden in {filename} gespeichert.")

    def plot_histogram(self):
        """Erstellt ein Histogramm der Briefanzahlen pro Tag."""
        plt.hist(self.data, bins=range(0, max(self.data) + 2), density=True, alpha=0.7, color="blue", edgecolor="black", label="Simulierte Daten")

        # Theoretische Poisson-Verteilung für Vergleich
        k_values = np.arange(0, max(self.data) + 1)
        poisson_pmf = stats.poisson.pmf(k_values, self.lambda_value)
        plt.plot(k_values, poisson_pmf, marker='o', linestyle='', color='red', label="Poisson-Theorie")

        plt.xlabel("Anzahl der Briefe pro Tag")
        plt.ylabel("Relative Häufigkeit")
        plt.title(f"Histogramm der Briefeingänge ({self.start_date.year}-{self.end_date.year}, λ={self.lambda_value})")
        plt.legend()
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

# Beispielhafte Nutzung:
if __name__ == "__main__":
    simulation = LetterSimulation(lambda_value=3, start_date="1781-01-01", end_date="1783-03-31", seed=42)
    simulation.generate_data()
    simulation.save_to_csv("./data/letters.csv")
    simulation.plot_histogram()
