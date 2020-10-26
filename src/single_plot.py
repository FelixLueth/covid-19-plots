import datetime
import matplotlib
import matplotlib.pyplot as plt
import argparse


def read_file(country):
  data = []
  with open('data/data_all.csv') as file:
    for line in file:
      if country in line:        
        data.append(line.strip().split(','))

  return reversed(data)


def create_plot(data, country, show_plot):
  dates = []
  cases = []
  deaths = []
  accumulation_cases = [0]
  accumulation_deaths = [0]

  for entry in data:
    dates.append(entry[0])
    cases.append(entry[4])
    deaths.append(entry[5])

  # Change cases from string to integer
  cases = list(map(int, cases))
  deaths = list(map(int, deaths))

  for x in range(1, len(cases)):
    accumulation_cases.append(accumulation_cases[x-1] + cases[x])
    accumulation_deaths.append(accumulation_deaths[x-1] + deaths[x])

  plt.figure(figsize=(20, 10), dpi=150)
  plt.plot(tuple(dates), cases, label='cases')
  plt.plot(tuple(dates), deaths, label='deaths')
  # plt.plot(tuple(dates), accumulation_cases, label='accumulated cases')
  # plt.plot(tuple(dates), accumulation_deaths, label='accumulated deaths')
  plt.title('Dailey Cases '+ country)
  plt.xlabel('Date')
  plt.ylabel('Cases')
  plt.legend()
  plt.yscale('linear')
  plt.tick_params(axis='x', rotation=-90)

  plt.savefig('output/daily_cases_' + country + '.png')
  
  if show_plot == True:
    print('show plot...')
    plt.show()


def main():
  
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--show', help='Specifies whether the plot will be displayed or not.', action='store_true')
  parser.add_argument('country', help='Specifies the country for the plot')
  args = parser.parse_args()
  
  
  COUNTRY = args.country
  show_plot = False
  
  if args.show:
    show_plot = True

  country_data_raw = read_file(COUNTRY)
  create_plot(country_data_raw, COUNTRY, show_plot)


main()
