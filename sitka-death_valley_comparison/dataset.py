import csv
from datetime import datetime

class Dataset():
    '''A class representing a single dataset.'''

    def __init__(self, filename):
        self.filename = filename

    def extract_data(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            dates, highs, lows = [], [], []
            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    dates.append(current_date)
                    highs.append(high)
                    lows.append(low)

            self.dates = dates
            self.highs = highs
            self.lows = lows




