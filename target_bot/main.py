import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

from product_monitor import check_stock

def main():
    
    PRODUCT = {
        1:{"sku":93954446, "url":"https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-prismatic-evolutions-booster-bundle/-/A-93954446#lnk=sametab"}
        }
    print(f"Checking the availability of {PRODUCT[1]["url"]}")

    check_stock(url=PRODUCT[1]["url"], sku=PRODUCT[1]["sku"])

if __name__ == "__main__":
    main()
