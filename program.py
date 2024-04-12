import pandas as pd
import os
import matplotlib.pyplot as plt

def test_run():
    # Define date range
    start_date = '2023-04-12'
    end_date = '2024-04-10'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    # Read 5 stocks data into temporary dataframe
    dfstock = pd.read_csv("STOCK_DATA_FINAL.csv", index_col="Date", parse_dates=True)

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfstock)

    return dfstock # Normalize by dividing by the first row


def plot_data(df1, title="Stock Prices"):
    '''Plot stock prices'''
    ax = df1.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Normalized Price")
    plt.show()

output = test_run()
plot_data(output)