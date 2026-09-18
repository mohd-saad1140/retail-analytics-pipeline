# Retail Data Automation & Analytics Pipeline

A lightweight data engineering pipeline that simulates an automated end-of-day retail ingestion engine. This project demonstrates backend integration between Python and a relational MySQL database.

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Database:** MySQL
- **Libraries:** mysql-connector-python

## ⚙️ How It Works
1. **Database Connection:** Establishes a direct connection socket using `mysql-connector-python`.
2. **Data Ingestion:** Iterates through structural data payloads wrapped inside primitive Python tuples and bulk inserts them into the table.
3. **Analytical Processing:** Uses SQL aggregate functions (SUM, GROUP BY, ORDER BY) to calculate total product revenues directly in the database.
4. **Dashboard Rendering:** Fetches the processed data and formats it cleanly in the terminal as an executive summary.

