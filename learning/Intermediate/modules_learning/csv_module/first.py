import csv

# Create new csv file and write some staff in it
with open('test.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['user_id', 'user_name', 'comments_qty'])
    writer.writerow([521, 'Matvii', 123])
    writer.writerow([522, 'Yaroslav', 813])
    writer.writerow([523, 'Svetlana', 420])

# Read csv file and print its content
with open('test.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    print(reader)
    print(type(reader))
    for line in reader:
        print(line)
    # csv_list = list(reader)
    # print(csv_list)
    for line in reader:
        # You get nothing because you can make iteration of reader only once
        print(line)
