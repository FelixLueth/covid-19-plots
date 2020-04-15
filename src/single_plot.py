import datetime
import matplotlib
import matplotlib.pyplot as plt
import sys

def read_file(country):
  data = []
  with open('data/data_all.csv') as file:
    for line in file:
      if country in line:        
        data.append(line.strip().split(','))

  return reversed(data)


def create_plot(data, country):
  dates = []
  cases = []
  for entry in data:
    dates.append(entry[0])
    cases.append(entry[4])

  # Change cases from string to integer
  cases = list(map(int, cases))

  plt.figure(figsize=(20, 10), dpi=150)
  plt.plot(tuple(dates), cases)
  plt.title('Dailey Cases '+ country)
  plt.xlabel('Date')
  plt.ylabel('Cases')
  plt.tick_params(axis='x', rotation=-90)

  plt.savefig('output/daily_cases_' + country + '.png')
  plt.show()


def main():
  COUNTRY = sys.argv[1]

  country_data_raw = read_file(COUNTRY)
  create_plot(country_data_raw, COUNTRY)


main()
