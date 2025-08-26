import pandas as pd
import matplotlib.pyplot as plt

def plot_trends():
    # Load trends data from the data folder
    df = pd.read_csv("data/trends_data.csv", parse_dates=["date"], index_col="date")

    # Plot
    df.plot(figsize=(10, 6))
    plt.title("Google Trends Data Over Time")
    plt.xlabel("Date")
    plt.ylabel("Trend")
    plt.legend(title="Keywords")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_trends()

