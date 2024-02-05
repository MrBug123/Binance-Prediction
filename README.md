```markdown
# Binance Price Prediction with Random Forest

📈 This Python script uses historical candlestick data from the Binance API to train a Random Forest classifier, predicting price movements for the next 4 periods.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MrBug123/Binance-Prediction.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Binance-Prediction
   ```

3. **Install required modules using `pip`:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the script:**
   ```bash
   python binance_price_prediction.py
   ```

2. **View the accuracy and prediction for the next 4 periods.**

## Features

- 📊 Fetches historical data from Binance API.
- 🤖 Trains a Random Forest classifier for price prediction.
- 📈 Evaluates model accuracy.
- 🚀 Predicts the next 4 periods.

## Additional Information

- **Binance API Endpoint:** [https://api.binance.com/api/v3/klines](https://api.binance.com/api/v3/klines)
- **Symbol:** BTCUSDT
- **Interval:** 5 minutes

### Note

- This script is for educational purposes and should not be used for actual trading.
- Always practice responsible algorithmic trading and consider the risks involved.
- Consult with financial experts before making any trading decisions.


