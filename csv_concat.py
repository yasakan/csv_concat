import codecs
import glob
import csv

if __name__ == "__main__":
    result = list()
    head = str()
    files = glob.glob('./csv/*.csv')
    
    for file in files:
        file_path = './csv/' + file.split('\\')[1]
        with codecs.open(file_path, 'r', 'utf-8-sig', 'ignore') as f:
            reader = csv.reader(f)
            head = next(reader)
            for row in reader:
                result.append(row)

    with codecs.open('./csv/all.csv', 'w', 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(head)
        writer.writerows(result)
