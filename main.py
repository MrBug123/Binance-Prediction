import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Binance API endpoint
binance_api_url = 'https://api.binance.com/api/v3/klines'

# Symbol and interval for the cryptocurrency data
symbol = 'BTCUSDT'
interval = '5m'

# Function to fetch historical candlestick data from Binance
def fetch_binance_data(symbol, interval, limit=100):
    params = {'symbol': symbol, 'interval': interval, 'limit': limit}
    response = requests.get(binance_api_url, params=params)
    data = response.json()
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Fetch historical data
historical_data = fetch_binance_data(symbol, interval, limit=100)

# Feature engineering (This part would be more sophisticated in a real-world scenario)
historical_data['target'] = historical_data['close'].shift(-4)  # Predict 4 periods into the future
historical_data['target'] = (historical_data['target'] > historical_data['close']).astype(int)

# Features (You may need to engineer more relevant features based on your strategy)
features = ['open', 'high', 'low', 'close', 'volume']

# Split data into training and testing sets
train_data, test_data = train_test_split(historical_data, test_size=0.2, shuffle=False)

# Train a simple Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(train_data[features], train_data['target'])

# Make predictions on the test set
predictions = clf.predict(test_data[features])

# Evaluate accuracy
accuracy = accuracy_score(test_data['target'], predictions)
print('Accuracy: {:.2%}'.format(accuracy))

# Predict the next 4 periods
latest_data = fetch_binance_data(symbol, interval, limit=5)
latest_features = latest_data[features].iloc[-1].values.reshape(1, -1)
prediction = clf.predict(latest_features)

if prediction == 1:
    print("The model predicts an increase in the next 4 periods.")
else:
    print("The model predicts a decrease or no change in the next 4 periods.")
