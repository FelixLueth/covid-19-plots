import datetime
import matplotlib
import matplotlib.pyplot as plt
import sys

def get_data(country, index):
  data_raw = []
  data = []
  with open('data/data_all.csv') as file:
    for line in file:
      if country in line:
        data_raw.append(line.strip().split(','))
        
  for entry in data_raw:
    if index == 0:
      data.append(entry[index])
    
    if index == 4:
      data.append(entry[index])
      
  return reversed(data)

def create_plot(dataset_one, dataset_two, dates, country_one, country_two):
  days = [x for x in range(0, len(dates))]
  
  plt.figure(figsize=(20, 10), dpi=150)
  plt.plot(days, dataset_one, label=country_one)
  plt.plot(days, dataset_two, label=country_two) 
  plt.title('Daily Cases  ' + country_one + ' and ' + country_two )
  plt.xlabel('Days since 01.01.2020')
  plt.ylabel('Cases')
  plt.legend()
  plt.tick_params(axis='x', rotation=-90)

  plt.savefig('output/daily_cases_' + country_one + '_' + country_two + '.png')
  # plt.show()


def main():
  COUNTRY_ONE = sys.argv[1]
  COUNTRY_TWO = sys.argv[2]

  dataset_one = list(map(int, get_data(COUNTRY_ONE, 4)))
  dataset_two = list(map(int, get_data(COUNTRY_TWO, 4)))

  dates = list(map(str,get_data(COUNTRY_ONE, 0)))

  create_plot(dataset_one, dataset_two, dates, COUNTRY_ONE, COUNTRY_TWO)


main()
