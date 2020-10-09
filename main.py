import math
import statistics

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def movies_mean(movies):
    return statistics.mean(movies)


def deviation(movies):
    return statistics.stdev(movies)


def dispersion(movies):
    return deviation(movies) ** 2


def movies_median(movies):
    return statistics.median(movies)


def movies_mode(movies):
    return statistics.multimode(movies)


def sample_span(movies):
    return max(movies) - min(movies)


def movies_quantiles(movies, q):
    return np.quantile(movies, q)


def without_zeros(criteria):
    return [i for i in criteria if i != 0 and not math.isnan(i)]


def lang_dict(info):
    dictionary = {}
    c = info['original_language'].to_list()
    for i in c:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary


def print_dict(dictionary):
    for i in dictionary.keys():
        print(i, ': ', dictionary[i])


def output_info(info, column_name):
    c = without_zeros(info[column_name].to_list())
    print(column_name.upper())
    print('Mean: ', movies_mean(c))
    print('Dispersion: ', dispersion(c))
    print('Deviation: ', deviation(c))
    print('Median: ', movies_median(c))
    print('Mode: ', movies_mode(c))
    print('Max value: ', max(c))
    print('Min value: ', min(c))
    print('Sample span: ', sample_span(c))
    print('Quantile 0.1: ', movies_quantiles(c, .10))
    print('Quantile 0.25: ', movies_quantiles(c, .25))
    print('Quantile 0.5: ', movies_quantiles(c, .50))
    print('Quantile 0.75: ', movies_quantiles(c, .75))
    print()
    print()


def histogram(info, horizontal_name, vertical_name):
    x = info[horizontal_name].to_list()
    y = info[vertical_name].to_list()

    plt.bar(x, y, label='first')

    plt.xlabel(horizontal_name)
    plt.ylabel(vertical_name)

    plt.title(f'Гистограмма зависимости ${vertical_name}$ от ${horizontal_name}$', fontsize=16)
    plt.legend()
    plt.show()


data = pd.read_csv('movies_csv.csv')
output_info(data, 'budget')
output_info(data, 'popularity')
output_info(data, 'revenue')
output_info(data, 'runtime')
output_info(data, 'vote_average')
output_info(data, 'vote_count')
print('LANGUAGES')
print_dict(lang_dict(data))

histogram(data, 'popularity', 'budget')
histogram(data, 'vote_average', 'budget')
histogram(data, 'vote_average', 'revenue')
histogram(data, 'vote_average', 'vote_count')
histogram(data, 'vote_average', 'runtime')
