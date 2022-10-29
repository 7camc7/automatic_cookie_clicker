from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/Users/claudiachurch/Desktop/web_dev/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min_timer = time.time() + 5 * 60

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
id_list = [item.get_attribute("id") for item in items]

while True:
    cookie.click()
    if time.time() > timeout:
        all_upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
        price_list = []
        for upgrade in all_upgrades:
            text = upgrade.text
            if text != "":
                upgrade_cost = text.split("-")[1].replace(",", "")
                price_list.append(int(upgrade_cost))

        upgrade_cookie = {}
        for n in range(len(price_list)):
            upgrade_cookie[price_list[n]] = id_list[n]

        cookie_total = driver.find_element(By.ID, "money").text
        if "," in cookie_total:
            cookie_total = cookie_total.replace(",", "")
        cookie_money = int(cookie_total)

        affordable_upgrades = {}
        for cost, id in upgrade_cookie.items():
            if cost < cookie_money:
                affordable_upgrades[cost] = id

        max_value = max(affordable_upgrades)
        upgrade_id = affordable_upgrades[max_value]
        driver.find_element(By.ID, f"{upgrade_id}").click()

        timeout = time.time() + 5

    if time.time() > five_min_timer:
        cookies_per_second = driver.find_element(By.ID, "cps").text
        print(cookies_per_second)
        break



# upgrade_list = []
# for price in upgrade_prices:
#     upgrade_list.append(price)




