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


def output_info(info, column_name, values_list=None):
    if values_list is None:
        c = without_zeros(info[column_name].to_list())
    else:
        c = values_list
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


def raw_to_bar_chart(info, horizontal_name, vertical_name):
    x = info[horizontal_name].to_list()
    y = info[vertical_name].to_list()

    plt.bar(x, y, label='first')

    plt.xlabel(horizontal_name)
    plt.ylabel(vertical_name)

    plt.title(f'Гистограмма зависимости ${vertical_name}$ от ${horizontal_name}$', fontsize=16)
    plt.legend()
    plt.show()


def dict_to_bar_chart(info):
    x = []
    y = []

    vertical_name = 'count'
    horizontal_name = 'language'

    for key in info:
        x.append(key)
        y.append(info[key])

    plt.bar(x, y, label='first')

    plt.xlabel(horizontal_name)
    plt.ylabel(vertical_name)

    plt.title(f'Гистограмма зависимости ${vertical_name}$ от ${horizontal_name}$', fontsize=16)
    plt.legend()
    plt.show()


def is_upper_case_letter(letter):
    return 'A' <= letter <= 'Z'


def get_weighted_ratings(info, avg_rating):
    vote_counts = info['vote_count'].to_list()
    minimum_number_of_votes = min(without_zeros(vote_counts))
    vote_avg = info['vote_average'].to_list()
    original_titles = info['original_title'].to_list()

    gens = dict()
    raw_genres = info['genres'].to_list()
    weighted_rates = []

    for i in range(len(vote_counts)):
        if vote_counts[i] == 0:
            continue
        rate = (1.0 * vote_counts[i] / (vote_counts[i] + minimum_number_of_votes) * vote_avg[i]) + \
               (1.0 * minimum_number_of_votes / (minimum_number_of_votes + vote_counts[i]) * avg_rating)
        name = original_titles[i]
        weighted_rates.append((rate, name))

        splitted = raw_genres[i].split('"')
        for word in splitted:
            if not is_upper_case_letter(word[0]):
                continue
            if word not in gens:
                gens[word] = [(rate, name)]
            else:
                if weighted_rates[-1] not in gens[word]:
                    gens[word].append(weighted_rates[-1])

    return weighted_rates, gens


def print_top_movies(movies, top):
    movies.sort(reverse=True)
    print(f'Top {top} movies:')
    for i in range(top):
        rate, name = movies[i]
        print(f'{i + 1}.', name, rate)
    print()


def print_top_genres(gens, top):
    for genre in gens.keys():
        print(f'Top {top} {genre} movies:')
        gens[genre].sort(reverse=True)
        for j in range(min(top, len(gens[genre]))):
            rate, name = gens[genre][j]
            print(f'{j + 1}.', name, rate)
        print()


# # user_input
# user_input = [int(i) for i in input().split()]
# print(sorted(user_input))
# output_info(None, 'statistics', user_input)

# def mean(listMovies):
#     summa = 0;
#     for i in range(len(listMovies)):
#         summa += listMovies[i]
#     return summa/len(listMovies)
#
#
# def dispersions(listMovies):
#     if len(listMovies) == 1:
#         return listMovies[0]
#     summa = 0
#     means = mean(listMovies)
#     for i in range(len(listMovies)):
#         value = listMovies[i] - means ** 2
#         summa += value
#     return summa / (len(listMovies) - 1)
#
#
# def deviations(listMovies):
#     return dispersions(listMovies) ** 0.5
#
#
# def medians(listMovies):
#     if len(listMovies) == 1:
#         return listMovies[0]
#     newl = sorted(listMovies);
#     n = len(listMovies)
#     if n % 2 == 0:
#         return newl[(n - 1) / 2]
#     else:
#         return (newl[n / 2 - 1] + newl[n / 2]) / 2
#
#
# def sample_spans(movies):
#     return max(movies) - min(movies)
#
#
def mode(movies):
    dictionary = {}
    for i in movies:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    maxim = max(dictionary.values())
    returnedList = []
    for i in range(dictionary.keys()):
        if i == maxim:
            returnedList.append(i)
    unique_items = set()
    for i in range(len(movies)):
        unique_items.add(i)
    if len(unique_items) == len(returnedList):
        print('Antimodal set')
        return
    return returnedList

#
# def quant(movies, quantils):
#     sorted_movies = sorted(movies)
#     q = quantils * len(sorted_movies)
#     rounded_coef = int(q)
#     return sorted_movies[rounded_coef]


# reading data
data = pd.read_csv('movies_csv.csv')

# statistics
output_info(data, 'budget')
output_info(data, 'popularity')
output_info(data, 'revenue')
output_info(data, 'runtime')
output_info(data, 'vote_average')
output_info(data, 'vote_count')

print('LANGUAGES')
print_dict(lang_dict(data))

# bar charts
raw_to_bar_chart(data, 'popularity', 'budget')
raw_to_bar_chart(data, 'vote_average', 'budget')
raw_to_bar_chart(data, 'vote_average', 'revenue')
raw_to_bar_chart(data, 'vote_average', 'vote_count')
raw_to_bar_chart(data, 'vote_average', 'runtime')
dict_to_bar_chart(lang_dict(data))

# popularity rate
vote_averages = data['vote_average'].to_list()
average_rating = sum(vote_averages) / len(vote_averages)

weighted_ratings, genres = get_weighted_ratings(data, average_rating)

print_top_movies(weighted_ratings, 10)
print_top_genres(genres, 5)

# average_rating = median
weighted_ratings, genres = get_weighted_ratings(data, statistics.mode(vote_averages))

print_top_movies(weighted_ratings, 10)
print_top_genres(genres, 5)
