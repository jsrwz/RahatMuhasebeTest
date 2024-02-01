import tkinter as tk
import datetime
import time
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DE
from selenium.common.exceptions import ElementNotInteractableException

arayuz = tk.Tk()
arayuz.title("Masraf girişleri")#title
arayuz.geometry("500x300")

tk.Label(text="Kaç tane masraf açacağınızı giriniz:").place(x=10,y=20)
y = tk.IntVar()
test_sayisi = tk.Entry(textvariable=y)
test_sayisi.place(x=200,y=20)

def masraflar():
    donme_sayisi = y.get()
    website = "http://kurulusdemo.rahatsistem.com.tr/account/login"

    d = DE.CHROME
    d['goog:loggingPrefs'] = { 'browser':'ALL' }
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver", desired_capabilities=d)
    driver.maximize_window() # For maximizing window
    # driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    def hatalar(path):
        try: 
            time.sleep(1)
            element_path = path
            WebDriverWait(driver, 8).until(
                EC.element_to_be_clickable((By.XPATH, element_path))
            )

            element_to_click = driver.find_element(By.XPATH,element_path)

            try:            
                driver.execute_script("arguments[0].click();", element_to_click)
            except ElementClickInterceptedException as err:
                print (err)
                time.sleep(2)
                driver.execute_script["arguments[0].click();", element_to_click]

            time.sleep(1)
                 
        except UnexpectedAlertPresentException as err:
            try:
                print ("Hata açıklaması:\n" + err.alert_text + "\n")
                error_time = datetime.datetime.now()
                print (f"Başlama zamanı: {once}")
                print (f"Hata zamanı: {error_time}")
                print("Toplam " + str(a) + " kayit oluşturuldu.")
                alert = driver.switch_to.alert
                alert.dismiss()
                time.sleep(3)
                
            except NoAlertPresentException:             
                driver.refresh()
                time.sleep(3)

        except:

            driver.refresh()
            print ("\nError Occured. Refreshing the page\n")
            time.sleep(3)

    driver.get(website)

    username_box = driver.find_element(By.XPATH, '//*[@id="username"]')
    username_box.send_keys("rahat_test1")
    password_box = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_box.send_keys("12345678")
    signIn_button = driver.find_element(By.XPATH, '//div[2]/div/form/button')
    driver.execute_script("arguments[0].click();", signIn_button)
    rahatmuhasebe = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[1]/div/a/div')
    driver.execute_script("arguments[0].click();", rahatmuhasebe)
    time.sleep(1)
    donem2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/a/div/div')
    donem2.click()
    varliklar = driver.find_element(By.XPATH, '//*[@id="def-assets-nav"]/a/span')
    driver.execute_script("arguments[0].click();", varliklar)
    masraflar = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/div/div/div/div[2]/a/button')
    driver.execute_script("arguments[0].click();", masraflar)

    #buraya kadar carilere giriyor


    def valueEntry(xpath, key):

        try:
            WebDriverWait(driver, 8).until(
                    EC.presence_of_element_located((By.XPATH, xpath))      
                )
            button = driver.find_element(By.XPATH, xpath)
            button.send_keys(key)

        except UnexpectedAlertPresentException as err:
            try:
                print ("Hata açıklaması:\n" + err.alert_text + "\n")
                error_time = datetime.datetime.now()
                print (f"Başlama zamanı: {once}")
                print (f"Hata zamanı: {error_time}")
                print("Toplam " + str(a) + " kayit oluşturuldu.")
                alert = driver.switch_to.alert
                alert.dismiss()
                time.sleep(3)
            
            except NoAlertPresentException:             
                driver.refresh()
                time.sleep(3)

        except:

            driver.refresh()
            print ("\nError Occured. Refreshing the page\n")
            time.sleep(3)

    value = "1"

    varlikadi_xpath = '//*[@id="name"]'
    aciklama_xpath = '//*[@id="new-item-description"]'
    yenimasraf_path = '//*[@id="column-search-datatable"]/div[1]/div/div/div[1]/button'
    kaydet_path = '//*[@id="new-expense-form"]/div[3]/button'

    a = 0

    once = datetime.datetime.now()

    for i in range (donme_sayisi):
        time.sleep(1)
        hatalar(yenimasraf_path)
        time.sleep(0.5)
        valueEntry(varlikadi_xpath, value)
        valueEntry(aciklama_xpath, value)
        time.sleep(0.5)
        hatalar(kaydet_path)


masraf_ac = tk.Button(text="Masraf açma",command=masraflar)
masraf_ac.place(x=100,y=50)

arayuz.mainloop()