# Import Libraries
import os
from datetime import datetime
import pandas as pd
from pycoingecko import CoinGeckoAPI
import boto3 #s3 connection python library

# Import internal scripts
from s3_file_upload import s3_file_upload
from crypto_api_extraction import crypto_api_extraction

def main():
    # Find current date for logging
    loaded_date = datetime.now().strftime('%Y-%m-%d')

    # List of cryptocurrency to pull
    coin_ids = ['bitcoin', 'ethereum', 'solana', 'dogecoin', 'cardano', 'xrp']

    CSV_FOLDER_PATH = f"C:/Users/Gianl/Desktop/Babbel/data-engineering.portfolio/crypto-pipeline/data-ingestion/crypto_reports/crypto_report_{loaded_date}.csv"

    crypto_api_extraction(FILE_PATH=CSV_FOLDER_PATH, crypto_list=coin_ids, current_date=loaded_date)

    # load data to s3 bucket
    s3_file_upload(CSV_FOLDER_PATH, "gg-crypto-data")

if __name__ == "__main__":
    main()
