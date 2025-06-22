import csv
import random
from datetime import datetime, timedelta

ASSETS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
TOTAL_RECORDS = 50000
RECORDS_PER_ASSET = TOTAL_RECORDS // len(ASSETS)
START_DATE = datetime(2010, 1, 1)

# Typical daily return parameters for equities
MU = 0.0003  # ~7% annual return
SIGMA = 0.02  # ~20% annual volatility


def generate_records():
    records = []
    for asset in ASSETS:
        price = 100.0 + random.random() * 20
        date = START_DATE
        for _ in range(RECORDS_PER_ASSET):
            open_p = price
            change = random.normalvariate(MU, SIGMA)
            close_p = open_p * (1 + change)
            high_p = max(open_p, close_p) * (1 + random.uniform(0, 0.02))
            low_p = min(open_p, close_p) * (1 - random.uniform(0, 0.02))
            volume = random.randint(1_000_000, 5_000_000)
            records.append([
                asset,
                date.strftime('%Y-%m-%d'),
                f'{open_p:.2f}',
                f'{high_p:.2f}',
                f'{low_p:.2f}',
                f'{close_p:.2f}',
                volume,
            ])
            price = close_p
            date += timedelta(days=1)
    return records


def main():
    records = generate_records()
    with open('data/market_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['asset', 'date', 'open', 'high', 'low', 'close', 'volume'])
        writer.writerows(records)


if __name__ == '__main__':
    random.seed(42)
    main()
