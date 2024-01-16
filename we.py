from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

def get_forex_rate(date, currency_code):
    if len(date) != 8 or not date.isdigit():
        print("错误的日期格式。请输入格式为YYYYMMDD的日期。")
        return

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.boc.cn/sourcedb/whpj/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pjname"))
        )

        date_input = driver.find_element(By.NAME, "erectDate")
        date_input.clear()
        date_input.send_keys(date)

        currency_input = driver.find_element(By.NAME, "nothing")
        currency_input.clear()
        currency_input.send_keys(currency_code)

        submit_button = driver.find_element(By.CLASS_NAME, "btn")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BOC_main"))
        )

        table = driver.find_element(By.CLASS_NAME, "BOC_main")
        rows = table.find_elements(By.TAG_NAME, "tr")

        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            if cols[0].text.strip() == currency_code:
                print(cols[3].text.strip())
                break
    except TimeoutException:
        print("请求超时，，，")
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用: python3 yourcode.py [日期YYYYMMDD] [货币代号]")
    else:
        date = sys.argv[1]
        currency_code = sys.argv[2].upper()
        get_forex_rate(date, currency_code)