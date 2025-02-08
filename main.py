import pandas as pd
import csv
from datetime import datetime

class CSV:
    CSV_FILE="finance_data.csv"
    COLUMNS={"date","amount","category","description"}

    @classmethod
    def initializeCSV(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }#dictionary
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("entry added")
CSV.initializeCSV()
CSV.add_entry("20-07-2024",125.65,"income","salary")