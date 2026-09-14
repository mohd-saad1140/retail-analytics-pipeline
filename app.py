import mysql.connector
from decimal import Decimal

def run_pipeline():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin@1234", 
            database="retail_analytics_db"
        )
        cursor = connection.cursor()

        # Database Setup
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_sales (
                product_name VARCHAR(100),
                quantity_sold INT,
                price_per_unit DECIMAL(10, 2),
                store_location VARCHAR(50)
            )
        """)

        # Data Ingestion
        new_transactions = [
            ('Wireless Mouse', 15, Decimal('1200.00'), 'Pune-Old'),
            ('Mechanical Keyboard', 5, Decimal('4500.00'), 'Pune-New'),
            ('HDMI Cable', 30, Decimal('350.00'), 'Pune-Old'),
            ('Gaming Headset', 8, Decimal('2500.00'), 'Pune-New'),
            ('Wireless Mouse', 10, Decimal('1200.00'), 'Pune-New'), 
            ('HDMI Cable', 12, Decimal('350.00'), 'Pune-New')
        ]

        insert_query = "INSERT INTO daily_sales VALUES (%s, %s, %s, %s)"
        for row in new_transactions:
            cursor.execute(insert_query, row)
            
        connection.commit()

        # Analytics Execution
        analytics_query = """
            SELECT product_name, SUM(quantity_sold), SUM(quantity_sold * price_per_unit) AS total_revenue
            FROM daily_sales
            GROUP BY product_name
            ORDER BY total_revenue DESC
        """
        cursor.execute(analytics_query)
        result = cursor.fetchall() 

        # Dashboard Output
        print("\n" + "="*56)
        print(f"{'PRODUCT PERFORMANCE DASHBOARD':^56}")
        print("="*56)
        print(f"{'Product Name':<22} | {'Units Sold':<10} | {'Total Revenue':<15}")
        print("-"*56)
        
        for row in result:
            print(f"{row[0]:<22} | {row[1]:^10} | ₹{row[2]:>12,.2f}")
            
        print("="*56)

    except mysql.connector.Error as error:
        print(f"❌ Error occurred: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    run_pipeline()
