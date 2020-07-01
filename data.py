import csv
with open('logscsv.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('logscsv.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['IP','Date','Time','URL','GET/POST','PORT'])
    w.writerows(data)