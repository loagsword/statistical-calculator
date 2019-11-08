import csv
from ClassFactory import class_factory
from Fileutilities.absolutepath import absolutepath


class CsvReader:
    data = []
    objects = []

    if data is not None:
        data.clear()

    if objects is not None:
        objects.clear()

    def __init__(self, filepath):
        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        for row in self.data:
            self.objects.append(class_factory(class_name, row))
        return self.objects
