import csv
#credit to https://stackoverflow.com/questions/72466218/ufeff-is-appearing-while-reading-csv-using-unicodecsv-module for the encoding fix

#load the distances to a 2d array
#space complexity is O(n)
#time complexity is O(n)
def load_distances():
    with open('data/distance.csv', encoding='utf-8-sig', newline='') as distFile:
        reader = csv.reader(distFile)
        distances = list(reader)
    return distances

distances = load_distances()