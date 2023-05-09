from selenium import webdriver
from csv import writer
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\webdivers\chromedriver.exe")
driver.get('https://bazarstore.az/search?controller=search&s=finish')


with open('bzs.csv', 'w', encoding="utf-8") as bzs_csv:
    csv_writer = writer(bzs_csv)
    csv_writer.writerow(['Name', 'Price'])
    
    
    mehsullar = driver.find_elements(By.CLASS_NAME, 'bs-product-row')
    for mehsul in mehsullar:
        Name = mehsul.find_element(By.CLASS_NAME, 'product-title').text
        pp,Price,textt = mehsul.find_element(By.CLASS_NAME, 'pp_price_with_text').text.split(" ")
                                                                                            


        csv_writer.writerow([Name, Price])


driver.quit()