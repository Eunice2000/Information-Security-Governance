USE customer_data;

CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  ssn VARCHAR(11),
  dob DATE,
  address VARCHAR(100),
  city VARCHAR(50),
  state VARCHAR(2),
  zip VARCHAR(10),
  email VARCHAR(100),
  phone VARCHAR(15),
  credit_card VARCHAR(16)
);

INSERT INTO customers
(first_name, last_name, ssn, dob, address, city, state, zip, email, phone, credit_card)
VALUES
  ('John', 'Doe', '123-45-6789', '1980-01-15', '123 Main St', 'Anytown', 'CA', '12345', 'john.doe@example.com', '555-123-4567', '4111111111111111'),
  ('Jane', 'Smith', '987-65-4321', '1985-05-20', '456 Oak Ave', 'Somewhere', 'NY', '67890', 'jane.smith@example.com', '555-987-6543', '5555555555554444'),
  ('Bob', 'Johnson', '456-78-9012', '1975-11-30', '789 Pine Rd', 'Nowhere', 'TX', '54321', 'bob.johnson@example.com', '555-456-7890', '3782822463100005');
