CREATE TABLE customers (
    id INT,
    name TEXT,
    email TEXT,
    created_at DATE
);

CREATE TABLE orders (
    id INT,
    customer_id INT,
    total DECIMAL,
    order_date DATE
);
