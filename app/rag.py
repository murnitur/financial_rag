import json
import random
from dotenv import load_dotenv
from faker import Faker

load_dotenv()

fake = Faker()

END = "\nEND\n"

SAVE_PATH = "database/finance_db"
INDEX_NAME = "financeIndexFAISS"


def generate_dataset(company_name: str, num_entries=20):
    data = []
    for _ in range(num_entries):
        entry = {
            "email": fake.email(),
            "phone_number": fake.basic_phone_number(),
            "ssn": fake.ssn(),
            "company": company_name,
            "quarter": random.choice(["Q1", "Q2", "Q3", "Q4"]),
            "year": random.choice([2021, 2022, 2023]),
            "revenue": round(random.uniform(500, 50000), 2),
            "profit": round(random.uniform(-500, 20000), 2),
            "operating_expenses": round(random.uniform(100, 15000), 2),
            "net_income": round(random.uniform(-1000, 10000), 2),
            "total_assets": round(random.uniform(500, 100000), 2),
            "total_liabilities": round(random.uniform(300, 60000), 2),
            "cash_flow_operating": round(random.uniform(0, 15000), 2),
            "cash_flow_investing": round(random.uniform(-10000, 5000), 2),
            "cash_flow_financing": round(random.uniform(-5000, 5000), 2),
            "eps": round(random.uniform(-5, 20), 2),  # Earnings per share
            "analyst_recommendation": random.choice(["Buy", "Hold", "Sell"]),
        }
        data.append(entry)
    return data


def generate_dataset_to_json(companies: list[str], num_entries_per_company=20):
    all_data = []
    for company in companies:
        all_data.append(
            generate_dataset(company_name=company, num_entries=num_entries_per_company)
        )

    # Dump to json file
    datasets = json.dumps(all_data, indent=4)
    with open("financial_data.json", "w") as json_file:
        json_file.write(datasets)

    return all_data


def load_financial_data(json_file_path):
    with open(json_file_path, "r") as f:
        data = json.load(f)
    return data


def prepare_financial_documents(data):
    documents = []
    for company_data in data:
        for entry in company_data:
            # Creating text representation of each data entry for embeddings and ending with a custom delimeter
            text = _getText(entry)
            documents.append(text)
    return documents


def embed():
    pass


def get_retriever():
    pass


def _getText(entry):
    return f"""Company: {entry['company']}
              Email: {entry['email']}
              SSN: {entry['ssn']}
              Phone: {entry['phone_number']}
              Year: {entry['year']}
              Quarter: {entry['quarter']}
              Revenue: {entry['revenue']} million
              Profit: {entry['profit']} million
              Operating Expenses: {entry['operating_expenses']} million
              Net Income: {entry['net_income']} million
              Total Assets: {entry['total_assets']} million
              Total Liabilities: {entry['total_liabilities']} million
              Cash Flow (Operating): {entry['cash_flow_operating']} million
              Cash Flow (Investing): {entry['cash_flow_investing']} million
              Cash Flow (Financing): {entry['cash_flow_financing']} million
              Earnings Per Share (EPS): {entry['eps']}
              Analyst Recommendation: {entry['analyst_recommendation']}
              {END}
              """
