# Answers To Question 2

* The number of orders made by each customer.
    * `SELECT COUNT(*) AS "Number Of Orders", "customer_id" FROM [Orders] GROUP BY "customer_id"`
* The list of all customers who have three or more orders.
    * `SELECT COUNT(*) AS "Number Of Orders", o.customer_id FROM [Orders] AS o WHERE o.customer_id > 2 GROUP BY "customer_id"`
* The list of all customers who have ordered the item named “test item”.
    * `SELECT *, o.customer_id FROM Orders AS o WHERE o.item_name == "test item" GROUP BY "customer_id"`
* The list of all customers who have NOT ordered the item named “test item”.
    * `SELECT *, o.customer_id FROM Orders AS o WHERE o.item_name != "test item" GROUP BY "customer_id"`

