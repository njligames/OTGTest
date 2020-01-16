import json
from datetime import datetime
from pprint import pprint
import unittest

def question4():
    input_file = 'data.json'
    number_month_dict = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
            }
    monthCount = {
            "January":0,
            "February":0,
            "March":0,
            "April":0,
            "May":0,
            "June":0,
            "July":0,
            "August":0,
            "September":0,
            "October":0,
            "November":0,
            "December":0,
            }
    with open(input_file) as json_file:
        data = json.load(json_file)
        for key, value in data.iteritems():
            datetime_object = datetime.strptime(value, '%m/%d/%Y')
            monthName = number_month_dict[datetime_object.month]
            monthCount[monthName] = monthCount[monthName] + 1

    return monthCount

class Test(unittest.TestCase):

    def test_question4(self):
        result = {'February': 0, 'October': 0, 'January': 2, 'April': 0, 'November': 0, 'March': 1, 'August': 0, 'May': 0, 'December': 1, 'June': 1, 'September': 0, 'July': 0}

        self.assertEqual(question4(), result)

if __name__ == '__main__':
    unittest.main()


