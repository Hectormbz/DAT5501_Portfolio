import pandas as pd
import matplotlib.pyplot as plt

def plotClosingPriceVsDate(filePath):
    # Read the CSV file
    df = pd.read_csv(filePath)

    # Convert the 'Date' column to datetime 
    df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

    # Ensure 'Close/Last' is float
    df['Close/Last'] = df['Close/Last'].str.replace('$','').astype(float)

     # Calculate the daily percentage change
    df['Daily Change (%)'] = df['Close/Last'].pct_change() * 100
 
    # Plot Daily Change percentage against Date
    plt.plot(df['Date'], df['Daily Change (%)'])
    plt.title('Daily Percentage Change vs Date')
    plt.xlabel('Date')
    plt.ylabel('Daily Change (%)')
    plt.grid(True)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout() 
    plt.show()

plotClosingPriceVsDate(r"C:\Users\hbuzzacott001\OneDrive - PwC\Uni work\YR2\DAT5501_Portfolio\asset prices\HistoricalData_1760959707604.csv")



