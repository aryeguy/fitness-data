import pandas
import os.path
import toolz
import re
import dateparser
import operator

# TODO extract zip of takeout

TAKEOUT_DIRECTORY_PATH = '/Users/guy/Downloads/Takeout'
CSV_DIRECTORY = 'Fit/Daily Aggregations'
csv_dir = os.path.join(TAKEOUT_DIRECTORY_PATH, CSV_DIRECTORY)
files = os.listdir(csv_dir)


def is_daily_aggregation(file_name):
    return re.match(r'\d{4}-\d{2}-\d{2}.csv', file_name)


daily_aggregations = toolz.filter(is_daily_aggregation, files)
data = []

for csv_file in daily_aggregations:
    date_part = csv_file.split(".")[0]
    date = dateparser.parse(date_part)
    csv = pandas.read_csv(os.path.join(csv_dir, csv_file))
    weight = csv[csv['Average weight (kg)'].notna()]['Average weight (kg)'].mean()
    if pandas.notna(weight):
        data.append({"date": date, "weight": weight})
        # print(csv_file, weight)
sorted_data = sorted(data, key=operator.itemgetter('date'))
df = pandas.DataFrame(sorted_data)
df.to_csv('output.csv')
print(sorted_data)
