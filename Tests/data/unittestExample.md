# Unit Test Example

## Note

There are three source files in this example.

1. Calculator.py : The Calculator.Calculator class is defined in Calculator.py. 
It has four function that implement two number’s plus, minus, multiple and divide function.

2. test.py : The TestCalculator class is defined in test.py. 
It is a unittest.TestCase class’s subclass. 
It open and load the test data from test_data.csv file in class level setup function. 
It close the test_data.csv file in class level teardown function. 
It also has four test function(test_plus, test_minus, test_multiple, test_divide) 
which test the Calculator.Calculator class’s related functions.

3. test_data.csv : This is a csv file that store test data. 
One row text in this file contains six column separated by comma. 
The first columns is the first number x, the second column is the second number y, 
the third column is the value of x+y, the fourth column is the value of x-y, the fifth column is the value of x*y, 
the sixth column is the value of x/y.


## Calculator.py

```Python
'''
This class provide 4 function to implement number, plus, minus, multiple and divide operation.
'''
class Calculator:
    def plus(self, x, y):
        return float(x) + float(y)

    def minus(self, x, y):
        return float(x) - float(y)

    def multiple(self, x, y):
        return float(x) * float(y)

    def divide(self, x, y):
        if int(y) is not 0:
            return float(x) / float(y)
         else:
            return 'error, divisor y can not be zero'

```

## test.py
```Python
import unittest, csv
import HtmlTestRunner
import xmlrunner

# the .py file name is Calculator and the class name is also Calculator
from Calculator import Calculator

# test data file path, the fils is a csv file.
test_data_file_path = './test_data.csv'

# test data file object
test_data_file_object = None

# test data row list.
test_data_row_list = list()

# load test data from ./test_data.csv file.
def load_test_data():
    global test_data_file_object, test_data_row_list
    # open test data csv file.
    test_data_file_object = open(test_data_file_path, 'r')
    # read the csv file and return the text line list.
    csv_reader = csv.reader(test_data_file_object, delimiter=',')

    for row in csv_reader:
        test_data_row_list.append(row)

    print('open and load data from test_data.csv complete.')

# close and release the test data file object.
def close_test_data_file():
    global test_data_file_object
    if test_data_file_object is not None:
        test_data_file_object.close()
        test_data_file_object = None
        print('close file test_data.csv complete.')

'''
This is the TestCase class that test Calculator class functions.
'''
class TestCalculator(unittest.TestCase):

    # this is the Calculator class instance.
    calculator = None

    # class level setup function, execute once only before any test function.
    @classmethod
    def setUpClass(cls):
        load_test_data()
        print('')
        print('setUpClass')

    # class level setup function, execute once only after all test function's execution.
    @classmethod
    def tearDownClass(cls):
        close_test_data_file()
        print('')
        print('tearDownClass')

    # execute before every test case function run.
    def setUp(self):
        self.calculator = Calculator()
        print('')
        print('setUp')

    # execute after every test case function run.
    def tearDown(self):
        # release the Calculator object.
        if self.calculator is not None:
            self.calculator = None
        print('')
        print('tearDown')


    # below are function that test Calculator class's plus, minus, multiple and divide functions.
    def test_plus(self):
        print('')
        print('******test_plus******')
        # get each row text from the csv file.
        for row in test_data_row_list:
            # the first column in the text line is x value.
            x = row[0]
            # the second column in the text line is y value.
            y = row[1]
            # the third column in the text line is (x + y) value.
            expect_result = row[2]
            result = self.calculator.plus(x, y)

            print(str(x) + ' + ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_minus(self):
        print('')
        print('******test_minus******')
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            # the fourth column in the text line is (x - y) value.
            expect_result = row[3]
            result = self.calculator.minus(x, y)

            print(str(x) + ' - ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_multiple(self):
        print('')
        print('******test_multiple******')
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            # the fifth column in the text line is (x * y) value.
            expect_result = row[4]
            result = self.calculator.multiple(x, y)

            print(str(x) + ' * ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))

    def test_divide(self):
        print('')
        print('******test_divide******')
        for row in test_data_row_list:
            x = row[0]
            y = row[1]
            # the sixth column in the text line is (x / y) value.
            expect_result = row[5]
            result = self.calculator.divide(x, y)

            print(str(x) + ' % ' + str(y) + ' = ' + str(result) + ', expect ' + str(expect_result))
            self.assertEqual(float(result), float(expect_result))


def build_test_suite():
    # create unittest.TestSuite object.
    test_suite = unittest.TestSuite()
    # add each test function to the test suite object.
    test_suite.addTest(TestCalculator('test_plus'))
    test_suite.addTest(TestCalculator('test_minus'))
    test_suite.addTest(TestCalculator('test_multiple'))
    test_suite.addTest(TestCalculator('test_divide'))
    return test_suite

def build_text_report():
    test_suite = build_test_suite()
    # create unittest.TextTestRunner() object.
    test_runner = unittest.TextTestRunner()
    # run the test suite.
    test_runner.run(test_suite)

    # run below code to run all test function
    # unittest.main()


# generate html report.
def build_html_report():
    test_suite = build_test_suite()
    test_runner = HtmlTestRunner.HTMLTestRunner(output='./html_report')
    test_runner.run(test_suite)

# generate xml result.
def build_xml_report():
    test_suite = build_test_suite()
    test_runner = xmlrunner.XMLTestRunner(output='./reports/xml_report')
    test_runner.run(test_suite)

if __name__ == "__main__":

    build_text_report()

    build_html_report()

    build_xml_report()
```