# news-pipeline

naija news data pipeline

# 📰 Daily Punch Headline Scraper (Airflow Project)

This project uses **Apache Airflow** to automate the daily scraping of top news headlines from [Punch Nigeria](https://punchng.com). It is designed as a modular ETL pipeline that can be extended to log results into a database, trigger notifications, or power downstream analytics.

---

## 🚀 Features

- Automated daily web scraping of Punch Nigeria headlines
- Modular architecture using a dedicated `scraper/` Python package
- Airflow DAG with schedule, task tagging, and logging
- Ready for database and notification integration
- Easy to deploy, run, and monitor

---

## 🗂️ Project Structure

airflow-project/
├── dags/
│ └── daily_news_pipeline.py # Airflow DAG definition
├── scraper/
│ ├── init.py
│ └── scrape_punch.py # Core scraping logic
├── airflow_venv/ # Python virtual environment (ignored by Git)
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mychail/news-pipeline.git
cd news-pipeline

# Create and activate a virtual environment
python3 -m venv airflow_venv
source airflow_venv/bin/activate

# Install Apache Airflow
export AIRFLOW_VERSION=2.8.1
export PYTHON_VERSION="$(python --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2)"
export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"


#Initialize Airflow

export AIRFLOW_HOME=~/airflow
airflow db init

# run airflow scheduler and Webserver
airflow scheduler
airflow webserver --port 8080
Access the Airflow UI at: http://localhost:8080


How It Works
The DAG daily_news_pipeline.py defines a daily task that runs the print_headlines() function.

That function uses the get_headlines() method from scraper.scrape_punch, which fetches and parses headline sections from Punch Nigeria.

Logs are viewable in the Airflow UI for each task run.

📥 Roadmap
✅ Scrape and print headlines to logs

🔜 Save scraped headlines to a SQL database (PostgreSQL or SQLite)

🔜 Send daily email or Telegram alerts with top headlines

🔜 Add basic NLP (e.g. topic clustering or sentiment tagging)

🔜 Create visual dashboard using Metabase, Superset, or Power BI

🧠 Technologies Used
Python 3.11+

Apache Airflow 2.8

Requests + BeautifulSoup

Bash scripting (for local deployment & sync)

📄 License
This project is open-source and licensed under the MIT License.

🙌 Contributing
want to improve this? Contributions are welcome! Please fork the repository and submit a pull request. Feedback, ideas, and feature suggestions are also appreciated.
```
