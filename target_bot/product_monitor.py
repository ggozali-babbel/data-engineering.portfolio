import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

def check_stock(url, sku):
    driver = uc.Chrome()
    driver.get(url)
    time.sleep(2)  # Let page load

    try:
        # Locate the button by its ID (from your HTML)
        button = driver.find_element(By.ID, f"addToCartButtonOrTextIdFor{sku}")
        # is_disabled = button.get_attribute("disabled") is not None
        if button.is_enabled():
            print("In Stock!")
            return True
    except:
        print("Out of Stock")
    
    driver.quit()
    return False
