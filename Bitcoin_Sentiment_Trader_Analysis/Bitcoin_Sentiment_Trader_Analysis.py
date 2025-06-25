# Bitcoin Market Sentiment vs Trader Performance
# ==============================================

# step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Step 2: Load the Datasets
trader_df = pd.read_csv("Task 1/historical_data.csv", parse_dates=["Timestamp IST"])
sentiment_df = pd.read_csv("Task 1/fear_greed_index.csv")

# Step 3: Clean & Convert Timestamps

# Trader data: convert Timestamp (ms) to datetime
trader_df['Timestamp'] = pd.to_numeric(trader_df['Timestamp'], errors='coerce')
trader_df['datetime'] = pd.to_datetime(trader_df['Timestamp'], unit='ms')
trader_df['date'] = trader_df['datetime'].dt.date

# Sentiment data: convert timestamp (s) to datetime
sentiment_df['timestamp'] = pd.to_numeric(sentiment_df['timestamp'], errors='coerce')
sentiment_df['datetime'] = pd.to_datetime(sentiment_df['timestamp'], unit='s')
sentiment_df['date'] = sentiment_df['datetime'].dt.date
sentiment_df['classification'] = sentiment_df['classification'].str.strip().str.title()

# Step 4: Merge the Datasets on 'date'
merged_df = pd.merge(trader_df, sentiment_df[['date', 'classification']], on='date', how='inner')

# Step 5: Feature Engineering
merged_df['Closed PnL'] = pd.to_numeric(merged_df['Closed PnL'], errors='coerce')
merged_df['Fee'] = pd.to_numeric(merged_df['Fee'], errors='coerce')
merged_df['profitable'] = merged_df['Closed PnL'] > 0

# Step 6: Analysis & Visualization

# Average PnL by sentiment
print("Average PnL by Sentiment:")
print(merged_df.groupby('classification')['Closed PnL'].mean())

# Profitability percentage by sentiment
print("\nProfitability Rate by Sentiment:")
print(merged_df.groupby('classification')['profitable'].mean())

# Boxplot: PnL by classification
sns.boxplot(x='classification', y='Closed PnL', data=merged_df)
plt.title("Closed PnL by Market Sentiment")
plt.show()

# Countplot: number of trades by sentiment
sns.countplot(x='classification', data=merged_df)
plt.title("Number of Trades by Market Sentiment")
plt.show()

# Step 7: Export merged data to CSV
merged_df.to_csv("final_trader_sentiment_data.csv", index=False)
print("\nMerged dataset saved as 'final_trader_sentiment_data.csv'")

