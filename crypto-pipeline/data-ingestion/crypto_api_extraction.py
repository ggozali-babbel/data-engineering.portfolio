import pandas as pd
from pycoingecko import CoinGeckoAPI

def crypto_api_extraction(FILE_PATH, crypto_list, current_date):
    # Initialize CoinGecko API client
    cg = CoinGeckoAPI()
    
    # List of cryptocurrency IDs
    coin_ids = ['bitcoin', 'ethereum', 'solana', 'dogecoin', 'cardano', 'xrp']

    # Fetch market data
    data = cg.get_coins_markets(
        vs_currency='usd',
        ids=coin_ids,
        order='market_cap_desc',
        per_page=100,
        page=1,
        price_change_percentage='24h'
    )

    # Convert to pandas DataFrame
    df = pd.DataFrame(data)

    # Select and rename relevant columns for readability --
    selected_columns = [
        'id', 'symbol', 'name', 'current_price', 'market_cap', 'total_supply',
        'ath', 'ath_date', 'atl', 'atl_date', 'price_change_percentage_24h'
    ]
    df_selected = df[selected_columns]

    # add loaded_date for logging
    df_selected['loaded_date'] = current_date

    # Convert data to .csv before uploading to s3 bucket
    df_selected.to_csv(FILE_PATH, index=False)

    