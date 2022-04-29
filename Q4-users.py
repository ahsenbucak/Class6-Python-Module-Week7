import csv

def print_names():
     with open("users.csv","r") as f_csv:
        reader = csv.reader(f_csv)
        for row in reader:
            print(row)

def add_name():
    with open('users.csv','a',newline='') as f_csv:
        writer = csv.writer(f_csv,dialect='excel')
        writer.writerow([input("Please enter a name:"),input("Please enter a surname:")])

add_name()
print_names()






