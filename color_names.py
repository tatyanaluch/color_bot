import pandas as pd
import re
import textdistance
from color import print_hex_color

columns = ['color_name', 'color_hex']
# TODO add multi-name support
names = pd.read_csv('color_names.txt', sep='\t', header=None, names=columns).drop_duplicates(subset='color_hex')
similarity_threshold = 0.75


def find_color_name(color_int):
    color = print_hex_color(color_int)
    for index, row in names.iterrows():
        if row['color_hex'] == color:
            words = re.findall('[A-Z][^A-Z]*', row['color_name'])
            result = ' '.join(words)
            return result

    return None


def find_color_by_name(name):
    name_to_search = name.replace(' ', '').lower()
    best_version = None
    best_similarity = 0

    for index, row in names.iterrows():
        version = row['color_name']
        similarity = textdistance.hamming.normalized_similarity(version.lower(), name_to_search)

        if similarity > best_similarity:
            best_similarity = similarity
            best_version = row['color_hex']

    if best_similarity >= similarity_threshold:
        return best_version, best_similarity

    return None


def find_color_by_name_exact(name):
    for index, row in names.iterrows():
        if row['color_name'] == name:
            return row['color_hex']
    return None

