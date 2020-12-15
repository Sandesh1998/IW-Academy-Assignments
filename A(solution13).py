# 13 . Write a function to write a comma-separated value(CSV) file.It should accept a file name and a list of tuples as parameters.The tuples should havea name,address,and age.
# The file should create a header row followed by a row for each tuple.
# If the following list of tuples was passed in:[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave',21)]
import csv
f = open("student.csv", "a", newline="")
tup1=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
writer = csv.writer(f)
writer.writerow(("name" , "address", "age"));
[writer.writerow(tup) for tup in tup1]
f.close()