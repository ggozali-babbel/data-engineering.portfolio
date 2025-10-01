import os
from dotenv import load_dotenv

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve your API key
    api_key = os.getenv("COINGECKO_API_KEY")

    if not api_key:
        raise ValueError("COINGECKO_API_KEY not found..")
    else:
        print(f"My API key is: {api_key}")

if __name__ == "__main__":
    main()
