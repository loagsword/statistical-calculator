from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean


from src.CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader(filepath)
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result


    def median(self):
        self.result = mean(self.data)
        return self.result

    def populationvariance(self):
        self.result = populationvariance(self.data)
        return self.result

    def zscore(self):
        self.result = zscore(self.data)
        return self.result

    def confidenceinterval(self):
        self.result = confidenceinterval(self.data)
        return self.result

    def standardizedscore(self):
        self.result = standardizedscore(self.data)
        return self.result

    def populationcorrelation(self):
         self.result = populationcorrelation(self.data)
         return self.result