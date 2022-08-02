from utilities.db.db_manager import dbManager

class Customers:
    @staticmethod
    def get_customer(email):
        print(email)
        return dbManager.fetch(f"SELECT * FROM customers WHERE email='{email}'")

    @staticmethod
    def signup_customer(email,password,full_name,neighbourhood,insta_url):
        return dbManager.commit(
            f"INSERT INTO customers (full_name, password,email,neighbourhood,insta_url) VALUES ('{full_name}', '{password}','{email}','{neighbourhood}', '{insta_url}')")



