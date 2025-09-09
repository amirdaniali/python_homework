## Amir Daniali
## Code the Dream
## Week 9
## Advanced SQL

from datetime import date
import sqlite3
import pathlib

BASEDIR = pathlib.Path(__file__).parent.parent
print(BASEDIR)


def task1(db_path: pathlib.Path | str) -> None:
    """Task 1: Complex JOINs with Aggregation

    Problem Statement:

    Find the total price of each of the first 5 orders.  There are several steps.  You need to join the orders table with the line_items table and the products table.  You need to GROUP_BY the order_id.  You need to select the order_id and the SUM of the product price times the line_item quantity.  Then, you ORDER BY order_id and LIMIT 5.  You don't need a subquery. Print out the order_id and the total price for each of the rows returned.

    Deliverable:
        Within the python_homework folder, create an assignment9 branch. Change to the assignment9 folder.
        Get the SQL statement working in sqlcommand.
        Within the assignment9 folder, create advanced_sql.py. This should open the database, issue the SQL statement, print out the result, and close the database.
        test your program.
    """
    try:

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT orders.order_id, SUM(products.price * line_items.quantity) AS total_price
        FROM orders
        JOIN line_items ON orders.order_id = line_items.order_id
        JOIN products ON line_items.product_id = products.product_id
        GROUP BY orders.order_id
        ORDER BY orders.order_id
        LIMIT 5;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("First 5 Orders and Their Total Prices:")
        for order_id, total_price in results:
            print(f"Order ID: {order_id}, Total Price: ${total_price:.2f}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()


def task2(db_path: pathlib.Path | str) -> None:
    """Task 2: Understanding Subqueries

    Problem Statement:

    For each customer, find the average price of their orders.  This can be done with a subquery. You compute the price of each order as in part 1, but you return the customer_id and the total_price.  That's the subquery. You need to return the total price using AS total_price, and you need to return the customer_id with AS customer_id_b, for reasons that will be clear in a moment.  In your main statement, you left join the customer table with the results of the subquery, using ON customer_id = customer_id_b.  You aliased the customer_id column in the subquery so that the column names wouldn't collide.  Then group by customer_id -- this GROUP BY comes after the subquery -- and get the average of the total price of the customer orders.  Return the customer name and the average_total_price.
    """
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        query = """
        SELECT customers.customer_name AS customer_name, AVG(order_totals.total_price) AS average_total_price
        FROM customers

        LEFT JOIN (
            SELECT orders.customer_id AS customer_id_b, SUM(products.price * line_items.quantity) AS total_price
            FROM orders
            JOIN line_items ON orders.order_id = line_items.order_id
            JOIN products ON line_items.product_id = products.product_id
            GROUP BY orders.order_id 
        ) AS order_totals

        ON customers.customer_id = order_totals.customer_id_b
        GROUP BY customers.customer_id
        ORDER BY customers.customer_name;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\n\nCustomer Name and Their Average Order Price:")
        for customer_name, avg_price in results:
            avg_display = f"${avg_price:.2f}" if avg_price is not None else "No Orders"
            print(f"{customer_name}: {avg_display}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()


def task3(db_path: pathlib.Path | str) -> None:
    """Task 3: An Insert Transaction Based on Data

    Problem Statement:

    You want to create a new order for the customer named Perez and Sons.  The employee creating the order is Miranda Harris.  The customer wants 10 of each of the 5 least expensive products.  You first need to do a SELECT statement to retrieve the customer_id, another to retrieve the product_ids of the 5 least expensive products, and another to retrieve the employee_id.  Then, you create the order record and the 5 line_item records comprising the order.  You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements. You have to use the order_id for the order record you created in the line_items records. The inserts must occur within the scope of one transaction. Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.

    You want to make sure that the foreign keys in the INSERT statements are valid.  So, add this line to your script, right after the database connection:

    conn.execute("PRAGMA foreign_keys = 1")

    In general, when creating a record, you don't want to specify the primary key.  So leave that column name off your insert statements.  SQLite will assign a unique primary key for you.  But, you need the order_id for the order record you insert to be able to insert line_item records for that order.  You can have this value returned by adding the following clause to the INSERT statement for the order:

    RETURNING order_id

    Deliverable:
        Get this working in sqlcommand. (Note that sqlcommand does not provide a way to begin and end transactions, so for sqlcommand, the creation of the order and line_item records are separate transactions.)
        Use sqlcommand to delete the line_items records for the order you created. (This is one delete statement.) Delete also the order record you created.
        Add statements for the complete transaction and the subsequent SELECT statement into advanced_py.sql, and to print out the result of the SELECT.
        Test your program.

    """
    try:

        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        conn.execute("BEGIN")

        cursor.execute(
            """SELECT customer_id 
            FROM customers 
            WHERE customer_name = ?""",
            ("Perez and Sons",),
        )
        customer_row = cursor.fetchone()
        if not customer_row:
            raise ValueError("Customer 'Perez and Sons' not found.")
        customer_id = customer_row[0]

        cursor.execute(
            "SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?",
            (
                "Miranda",
                "Harris",
            ),
        )
        employee_row = cursor.fetchone()
        if not employee_row:
            raise ValueError("Employee 'Miranda Harris' not found.")
        employee_id = employee_row[0]

        cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
        product_rows = cursor.fetchall()
        product_ids = [row[0] for row in product_rows]

        current_date = date.today().isoformat()

        # See SQLite Returning Clause
        # https://sqlite.org/lang_returning.html
        cursor.execute(
            """
            INSERT INTO orders (customer_id, employee_id, date)
            VALUES (?, ?, ?)
            RETURNING order_id
            """,
            (customer_id, employee_id, current_date),
        )
        order_id = cursor.fetchone()[0]

        for product_id in product_ids:
            cursor.execute(
                """INSERT INTO line_items (order_id, product_id, quantity)
                VALUES (?, ?, ?)""",
                (order_id, product_id, 10),
            )

        conn.commit()

        cursor.execute(
            """SELECT line_items.line_item_id, line_items.quantity, products.product_name
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
            WHERE line_items.order_id = ?""",
            (order_id,),
        )
        results = cursor.fetchall()

        print(f"\n\nOrder ID {order_id} - Line Items:")
        for line_item_id, quantity, product_name in results:
            print(
                f"Line Item ID: {line_item_id}, Quantity: {quantity}, Product: {product_name}"
            )

    except Exception as e:
        conn.rollback()
        print(f"Task 3: Error: {e}")
    finally:
        if conn:
            conn.close()


def task4(db_path: pathlib.Path | str) -> None:
    """Task 4: Aggregation with HAVING

    Problem Statement:

    Find all employees associated with more than 5 orders.  You want the first_name, the last_name, and the count of orders.  You need to do a JOIN on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.

    Deliverable:
        Get it working in sqlcommand.
        Add code advanced_sql.py to print out the employee_id, first_name, last_name, and an order count for each of the employees with more than 5 orders.
        Test your program.
    """

    try:
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        query = """
        SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS order_count
        FROM employees
        JOIN orders ON employees.employee_id = orders.employee_id
        GROUP BY employees.employee_id
        HAVING COUNT(orders.order_id) > 5
        ORDER BY order_count DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("\n\nEmployees with more than 5 orders:")
        for first_name, last_name, count in results:
            print(f"{first_name} {last_name}: {count} orders")

    except sqlite3.Error as e:
        print(f"Task 4 : Database error: {e}")
    except Exception as e:
        print(f"Task 4 : Unexpected error: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    task1(BASEDIR / "db/lesson.db")
    task2(BASEDIR / "db/lesson.db")
    task3(BASEDIR / "db/lesson.db")
    task4(BASEDIR / "db/lesson.db")
