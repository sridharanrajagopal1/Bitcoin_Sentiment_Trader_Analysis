# 📊 Bitcoin Market Sentiment vs Trader Performance

This project explores the relationship between Bitcoin market sentiment (Fear/Greed) and trader performance, using historical trader data from Hyperliquid and a Bitcoin Fear & Greed Index dataset.

---

## 🚀 Objective

To analyze how emotional market states like **Fear** and **Greed** influence:
- Trader profitability
- Risk behavior (leverage usage)
- Trade volume and direction (Buy/Sell)

We aim to uncover **actionable insights** to support smarter trading decisions.

---

## 📁 Datasets Used

### 1. 🧠 Bitcoin Market Sentiment Dataset
- `Date`: Date of sentiment reading
- `Classification`: Sentiment value (Fear or Greed)

### 2. 📈 Hyperliquid Trader Data
- `account`, `symbol`, `execution price`, `size`, `side`
- `closedPnL`, `leverage`, `direction`, `timestamp`, etc.

---

## 🛠️ Tools & Technologies

- **Python**: Data cleaning, preprocessing, merging
- **Pandas / Seaborn / Matplotlib**: Analysis and visualization
- **Power BI**: Dashboard development
- *(Optional)* SQL for queries if loaded into PostgreSQL

---

## 📊 Key Features

- Timestamp standardization (ms & s)
- Data merge on trade date and sentiment date
- Metrics calculated:
  - Average PnL by sentiment
  - Profitability rate
  - Avg. leverage by emotion
  - Behavior of Buy vs Sell under emotion
- Exportable merged dataset for Power BI
- PDF Report with findings

---

## 📌 Insights Discovered

- Trades on **Greed** days are more profitable (avg PnL ↑)
- **Fear** days show higher use of leverage but more losses
- **Short positions** more common in Fear periods, often less successful
- Power BI dashboard reveals trends clearly across time and accounts

---

## 📁 File Structure

📦 sentiment-trader-analysis/
├── trader_data.csv
├── sentiment_data.csv
├── final_trader_sentiment_data.csv
├── Bitcoin_Sentiment_Trader_Analysis.ipynb
├── Bitcoin_Sentiment_Trader_Analysis.py
├── Bitcoin_Trader_Sentiment_Report.pdf
├── mock_trader_sentiment_data.csv
└── README.md

yaml
Copy
Edit

---

## 📷 Sample Dashboard (Power BI)
> *Include screenshot of your Power BI dashboard here*

---

## 🧠 How to Use

1. Clone this repo  
2. Run the Jupyter Notebook or `.py` script to generate `final_trader_sentiment_data.csv`
3. Import into Power BI using mock or real data
4. Explore KPIs, filters, and visual insights

---

## ✅ Authors

**Sridharan Rajagopal**  
🔗 [LinkedIn](https://www.linkedin.com/in/sridharan-rajagopal)  
📁 [Portfolio](https://portfolio-demo-sridharanrajagopal1s-projects.vercel.app/)  
🐍 [GitHub](https://github.com/sridharanrajagopal1)

---

## 📃 License

This project is for educational and demo purposes only.
