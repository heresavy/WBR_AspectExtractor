import csv

#----------------------------------------------------------------------

def csv_dict_reader(file_obj):

    """

    Read a CSV file using csv.DictReader

    """

    reader = csv.DictReader(file_obj, delimiter='|')

    for line in reader:

        print(line["asin"]),

        print(line["reviewText"])

#----------------------------------------------------------------------

if __name__ == "__main__":

    with open("C:\\Users\\Saurav Karmakar\\Downloads\\AspectExtraction\\dataset\\data\\10.csv") as f_obj:

        csv_dict_reader(f_obj)