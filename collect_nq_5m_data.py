import tradingview_ta as ta
import pandas as pd

# Define the symbol and timeframe
symbol = "NQ"
timeframe = "5m"

# Function to fetch data from TradingView
def fetch_data(symbol, timeframe):
    analysis = ta.TA_Handler(
        symbol=symbol,
        screener="america",
        exchange="NASDAQ",
        interval=timeframe
    )
    return analysis.get_analysis().indicators

# Function to calculate DR statistics
def calculate_dr_statistics(data):
    # Example calculations (customize as needed)
    dr_high = max(data['high'])
    dr_low = min(data['low'])
    dr_true_percentage = (dr_high - dr_low) / dr_low * 100
    retracement = (data['close'][-1] - dr_low) / (dr_high - dr_low) * 100
    return {
        "DR High": dr_high,
        "DR Low": dr_low,
        "DR True Percentage": dr_true_percentage,
        "Retracement": retracement
    }

# Collect data and calculate statistics
data = fetch_data(symbol, timeframe)
stats = calculate_dr_statistics(data)

# Convert results to DataFrame and save to CSV
df = pd.DataFrame([stats])
df.to_csv("nq_5m_dr_statistics.csv", index=False)

print("Data collection complete. Results saved to nq_5m_dr_statistics.csv")
