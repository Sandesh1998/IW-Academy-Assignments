# 14 .Write a function that reads a CSV file.
# It should return a list of dictionaries,using the first row as keynames,and each subsequent row as values for those keys.
import csv
import sys

a_csv_file=open("student.csv", "rt")
dict_reader=csv.DictReader(a_csv_file)
print([ row for row in dict_reader])

