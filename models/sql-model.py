from mysql import connect


create_table_deals = """
CREATE TABLE deals IF NOT EXISTS
(
    phone_number INT UNSIGNED
    service CHAR
    quantity INT
    datetime DECIMAL(10, 2)
);
"""

create_table_customers = """
CREATE TABLE customers IF NOT EXISTS
(
    phone_number INT UNSIGNED
    last_name CHAR
    first_name CHAR
    father_name CHAR
    sex BOOL
    city CHAR
    address CHAR
    comment CHAR
)
"""

create_table_prices = """
CREATE TABLE prices IF NOT EXISTS
(
    product CHAR
    quantity DECIMAL(5, 2)
    price_rub INT
)
"""
