import csv

peopledata = ['John', '502-77-3056', '2/27/1985', 117.45]

with open('people.csv', 'w') as people:
    peoplewriter =  csv.writer(people)
    peoplewriter.writerow(peopledata)

"""
    Creates a file that looks like this:

    John,502-77-3056,2/27/1985,117.45

"""
