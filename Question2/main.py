#/bin/python
# -*- coding: utf-8 -*-

import sqlite3

question_a = '''
SELECT COUNT(*) AS "Number Of Orders", "customer_id" FROM [Orders] GROUP BY "customer_id"
'''

question_b = '''
SELECT COUNT(*) AS "Number Of Orders", o.customer_id FROM [Orders] AS o WHERE o.customer_id > 2 GROUP BY "customer_id"
'''

question_c = '''
SELECT *, o.customer_id FROM Orders AS o WHERE o.item_name == "test item" GROUP BY "customer_id"
'''

question_d = '''
SELECT *, o.customer_id FROM Orders AS o WHERE o.item_name != "test item" GROUP BY "customer_id"
'''

databasepath = "Question2.db"

def question(query):
    ret = None
    try:
        conn = sqlite3.connect(databasepath)
        conn.text_factory = str

        cur = conn.cursor()
        cur.execute(query)
        ret = cur.fetchall()

        conn.commit()
        conn.close
    except sqlite3.Error as e:
        print "An error occurred:" , e.args[0]

    return ret

def populateOrdersTable():
    try:
        conn = sqlite3.connect(databasepath)
        conn.text_factory = str
        for t in [
                (10248, 90, "Chais"),
                (10249, 81, "Chang"),
                (10250, 34, "Aniseed Syrup"),
                (10251, 84, "Chef Anton's Cajun Seasoning"),
                (10252, 76, "Chef Anton's Gumbo Mix"),
                (10253, 34, "Grandma's Boysenberry Spread"),
                (10254, 14, "Uncle Bob's Organic Dried Pears"),
                (10255, 68, "Northwoods Cranberry Sauce"),
                (10256, 88, "Mishi Kobe Niku"),
                (10257, 35, "Ikura"),
                (10258, 20, "Queso Cabrales"),
                (10259, 13, "Queso Manchego La Pastora"),
                (10260, 55, "Konbu"),
                (10261, 61, "Tofu"),
                (10262, 65, "Genen Shouyu"),
                (10263, 20, "Pavlova"),
                (10264, 24, "Alice Mutton"),
                (10265, 7 , "Carnarvon Tigers"),
                (10266, 87, "Teatime Chocolate Biscuits"),
                (10267, 25, "Sir Rodney's Marmalade"),
                (10268, 33, "Sir Rodney's Scones"),
                (10269, 89, "Gustaf's Knäckebröd"),
                (10270, 87, "Tunnbröd"),
                (10271, 75, "Guaraná Fantástica"),
                (10272, 65, "NuNuCa Nuß-Nougat-Creme"),
                (10273, 63, "Gumbär Gummibärchen"),
                (10274, 85, "Schoggi Schokolade"),
                (10275, 49, "Rössle Sauerkraut"),
                (10276, 80, "Thüringer Rostbratwurst"),
                (10277, 52, "Nord-Ost Matjeshering"),
                (10278, 5 , "Gorgonzola Telino"),
                (10279, 44, "Mascarpone Fabioli"),
                (10280, 5 , "Geitost"),
                (10281, 69, "Sasquatch Ale"),
                (10282, 69, "Steeleye Stout"),
                (10283, 46, "Inlagd Sill"),
                (10284, 44, "Gravad lax"),
                (10285, 63, "Côte de Blaye"),
                (10286, 63, "Chartreuse verte"),
                (10287, 67, "Boston Crab Meat"),
                (10288, 66, "Jack's New England Clam Chowder"),
                (10289, 11, "Singaporean Hokkien Fried Mee"),
                (10290, 15, "Ipoh Coffee"),
                (10291, 61, "Gula Malacca"),
                (10292, 81, "Røgede sild"),
                (10293, 80, "Spegesild"),
                (10294, 65, "Zaanse koeken"),
                (10295, 85, "Chocolade"),
                (10296, 46, "Maxilaku"),
                (10297, 7 , "Valkoinen suklaa"),
                (10298, 37, "Manjimup Dried Apples"),
                (10299, 67, "Filo Mix"),
                (10300, 49, "Perth Pasties"),
                (10301, 86, "Tourtière"),
                (10302, 76, "Pâté chinois"),
                (10303, 30, "Gnocchi di nonna Alice"),
                (10304, 80, "Ravioli Angelo"),
                (10305, 55, "Escargots de Bourgogne"),
                (10306, 69, "Raclette Courdavault"),
                (10307, 48, "Camembert Pierrot"),
                (10308, 2 , "Sirop d'érable"),
                (10309, 37, "Tarte au sucre"),
                (10310, 77, "Vegie-spread"),
                (10311, 18, "Wimmers gute Semmelknödel"),
                (10312, 86, "Louisiana Fiery Hot Pepper Sauce"),
                (10313, 63, "Louisiana Hot Spiced Okra"),
                (10314, 65, "Laughing Lumberjack Lager"),
                (10315, 38, "Scottish Longbreads"),
                (10316, 65, "Gudbrandsdalsost"),
                (10317, 48, "Outback Lager"),
                (10318, 38, "Fløtemysost"),
                (10319, 80, "Mozzarella di Giovanni"),
                (10320, 87, "Röd Kaviar"),
                (10321, 38, "Longlife Tofu"),
                (10322, 58, "Rhönbräu Klosterbier"),
                (10323, 39, "Lakkalikööri"),
                (10324, 71, "Original Frankfurter grüne Soße"),
                (10325, 39, "Chais"),
                (10326, 8 , "Chang"),
                (10327, 24, "Aniseed Syrup"),
                (10328, 28, "Chef Anton's Cajun Seasoning"),
                (10329, 75, "Chef Anton's Gumbo Mix"),
                (10330, 46, "Grandma's Boysenberry Spread"),
                (10331, 9 , "Uncle Bob's Organic Dried Pears"),
                (10332, 51, "Northwoods Cranberry Sauce"),
                (10333, 87, "Mishi Kobe Niku"),
                (10334, 84, "Ikura"),
                (10335, 37, "Queso Cabrales"),
                (10336, 60, "Queso Manchego La Pastora"),
                (10337, 25, "Konbu"),
                (10338, 55, "Tofu"),
                (10339, 51, "Genen Shouyu"),
                (10340, 9 , "Pavlova"),
                (10341, 73, "Alice Mutton"),
                (10342, 25, "Carnarvon Tigers"),
                (10343, 44, "Teatime Chocolate Biscuits"),
                (10344, 89, "Sir Rodney's Marmalade"),
                (10345, 63, "Sir Rodney's Scones"),
                (10346, 65, "Gustaf's Knäckebröd"),
                (10347, 21, "Tunnbröd"),
                (10348, 86, "Guaraná Fantástica"),
                (10349, 75, "NuNuCa Nuß-Nougat-Creme"),
                (10350, 41, "Gumbär Gummibärchen"),
                (10351, 20, "Schoggi Schokolade"),
                (10352, 28, "Rössle Sauerkraut"),
                (10353, 59, "Thüringer Rostbratwurst"),
                (10354, 58, "Nord-Ost Matjeshering"),
                (10355, 4 , "Gorgonzola Telino"),
                (10356, 86, "Mascarpone Fabioli"),
                (10357, 46, "Geitost"),
                (10358, 41, "Sasquatch Ale"),
                (10359, 72, "Steeleye Stout"),
                (10360, 7 , "Inlagd Sill"),
                (10361, 63, "Gravad lax"),
                (10362, 9 , "Côte de Blaye"),
                (10363, 17, "Chartreuse verte"),
                (10364, 19, "Boston Crab Meat"),
                (10365, 3 , "Jack's New England Clam Chowder"),
                (10366, 29, "Singaporean Hokkien Fried Mee"),
                (10367, 83, "Ipoh Coffee"),
                (10368, 20, "Gula Malacca"),
                (10369, 75, "Røgede sild"),
                (10370, 14, "Spegesild"),
                (10371, 41, "Zaanse koeken"),
                (10372, 62, "Chocolade"),
                (10373, 37, "Maxilaku"),
                (10374, 91, "Valkoinen suklaa"),
                (10375, 36, "Manjimup Dried Apples"),
                (10376, 51, "Filo Mix"),
                (10377, 72, "Perth Pasties"),
                (10378, 24, "Tourtière"),
                (10379, 61, "Pâté chinois"),
                (10380, 37, "Gnocchi di nonna Alice"),
                (10381, 46, "Ravioli Angelo"),
                (10382, 20, "Escargots de Bourgogne"),
                (10383, 4 , "Raclette Courdavault"),
                (10384, 5 , "Camembert Pierrot"),
                (10385, 75, "Sirop d'érable"),
                (10386, 21, "Tarte au sucre"),
                (10387, 70, "Vegie-spread"),
                (10388, 72, "Wimmers gute Semmelknödel"),
                (10389, 10, "Louisiana Fiery Hot Pepper Sauce"),
                (10390, 20, "Louisiana Hot Spiced Okra"),
                (10391, 17, "Laughing Lumberjack Lager"),
                (10392, 59, "Scottish Longbreads"),
                (10393, 71, "Gudbrandsdalsost"),
                (10394, 36, "Outback Lager"),
                (10395, 35, "Fløtemysost"),
                (10396, 25, "Mozzarella di Giovanni"),
                (10397, 60, "Röd Kaviar"),
                (10398, 71, "Longlife Tofu"),
                (10399, 83, "Rhönbräu Klosterbier"),
                (10400, 19, "Lakkalikööri"),
                (10401, 65, "Original Frankfurter grüne Soße"),
                (10402, 20, "Chais"),
                (10403, 20, "Chang"),
                (10404, 49, "Aniseed Syrup"),
                (10405, 47, "Chef Anton's Cajun Seasoning"),
                (10406, 62, "Chef Anton's Gumbo Mix"),
                (10407, 56, "Grandma's Boysenberry Spread"),
                (10408, 23, "Uncle Bob's Organic Dried Pears"),
                (10409, 54, "Northwoods Cranberry Sauce"),
                (10410, 10, "Mishi Kobe Niku"),
                (10411, 10, "Ikura"),
                (10412, 87, "Queso Cabrales"),
                (10413, 41, "Queso Manchego La Pastora"),
                (10414, 21, "Konbu"),
                (10415, 36, "Tofu"),
                (10416, 87, "Genen Shouyu"),
                (10417, 73, "Pavlova"),
                (10418, 63, "Alice Mutton"),
                (10419, 68, "Carnarvon Tigers"),
                (10420, 88, "Teatime Chocolate Biscuits"),
                (10421, 61, "Sir Rodney's Marmalade"),
                (10422, 27, "Sir Rodney's Scones"),
                (10423, 31, "Gustaf's Knäckebröd"),
                (10424, 51, "Tunnbröd"),
                (10425, 41, "Guaraná Fantástica"),
                (10426, 29, "NuNuCa Nuß-Nougat-Creme"),
                (10427, 59, "Gumbär Gummibärchen"),
                (10428, 66, "Schoggi Schokolade"),
                (10429, 37, "Rössle Sauerkraut"),
                (10430, 20, "Thüringer Rostbratwurst"),
                (10431, 10, "Nord-Ost Matjeshering"),
                (10432, 75, "Gorgonzola Telino"),
                (10433, 60, "Mascarpone Fabioli"),
                (10434, 24, "Geitost"),
                (10435, 16, "Sasquatch Ale"),
                (10436, 7 , "Steeleye Stout"),
                (10437, 87, "Inlagd Sill"),
                (10438, 79, "Gravad lax"),
                (10439, 51, "Côte de Blaye"),
                (10440, 71, "Chartreuse verte"),
                (10441, 55, "Boston Crab Meat"),
                (10442, 20, "Jack's New England Clam Chowder"),
                (10443, 66, "Singaporean Hokkien Fried Mee"),
                (10444, 66, "test item"),
                ]:
            conn.execute('insert into orders values (?,?,?)', t)

        # conn.execute("INSERT INTO Orders(id, customer_id, item_name) %i, %i, %s)" % (10248, 90, "Chais"))
        conn.commit()
        conn.close
    except sqlite3.Error as e:
        print "An error occurred:" , e.args[0]



print(question(question_a))
print(question(question_b))
print(question(question_c))
print(question(question_d))

# populateOrdersTable()
