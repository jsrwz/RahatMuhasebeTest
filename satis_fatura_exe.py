import tkinter as tk
import time
import datetime
import random
from getpaths import getpath
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

arayuz = tk.Tk()
arayuz.title("Satış faturası girişleri")#title
arayuz.geometry("500x300") #boyut

tk.Label(text="Kaç tane satış faturası açacağınızı giriniz:").place(x=10,y=20)
y = tk.IntVar()
test_sayisi = tk.Entry(textvariable=y)
test_sayisi.place(x=225,y=20)

def satislar():
    donme_sayisi = y.get()
    website = "https://kurulusdemo.rahatsistem.com.tr/account/login"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options, executable_path="Users/usAme/Downloads/chromedriver")
    driver.maximize_window() # For maximizing window
    # driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

    actions = ActionChains(driver)

    def click(xpath):

        x = driver.find_element(By.XPATH, xpath)
        x.click()

    def sendkeys(xpath, keys):

        x = driver.find_element(By.XPATH, xpath)
        x.send_keys(keys)

    def randomFloat():

        return random.uniform(1,100)
        
    def randomInt():

        return random.randrange(1,50)

    def randomInt10():

        return random.randrange(1,10)

    driver.get(website)
    kullanici_adi = driver.find_element(By.XPATH , '//*[@id="username"]')
    kullanici_adi.send_keys("rahat_test1")
    sifre = driver.find_element(By.XPATH, '//*[@id="password"]')
    sifre.send_keys("12345678")
    giris = driver.find_element(By.XPATH, '//div[2]/div/form/button')
    driver.execute_script("arguments[0].click();", giris)
    time.sleep(1)
    rahatmuhasebe = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[1]/div/a/div')
    driver.execute_script("arguments[0].click();", rahatmuhasebe)
    time.sleep(1)
    donem2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[2]/div[2]/div[2]/a/div/div')
    driver.execute_script("arguments[0].click();", donem2)
    time.sleep(1)

    #alislar

    satislar_xpath = '//*[@id="move-sells-nav"]/a/span'
    click (satislar_xpath)
    time.sleep(0.5)

    #yeni_alis
    yenisatis_xpath = '/html/body/div[4]/div[3]/div/div[1]/div[2]/a/button/span'
    yenisatis_buton = driver.find_element(By.XPATH, yenisatis_xpath)
    driver.execute_script("arguments[0].click();", yenisatis_buton)
    time.sleep(1)

    startTime = datetime.datetime.now()

    for i in range (donme_sayisi):

        #cari_sec
        cari_sec = '//*[@id="customer-name"]' 
        cari_secimi = driver.find_element(By.XPATH,cari_sec)
        driver.execute_script("arguments[0].click();", cari_secimi)
        time.sleep(1)

        #tedarikci_cari_ara
        cari_ara = driver.find_element(By.XPATH, '//*[@id="select2-customer-select-container"]') 
        cari_ara.click()
        time.sleep(1)

        #tedarikci_cari_sec
        tedarikci_cari_sec = driver.find_element(By.XPATH, '//*[@id="customer-select-modal"]/div/div/div[2]/div/span[2]/span/span[1]/input')
        tedarikci_cari_sec.send_keys("11")
        time.sleep(0.5)
        tedarikci_cari_sec.send_keys(Keys.ENTER)
        actions=ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()

        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)

        #cari seç ve onayla
        cari_onay = driver.find_element(By.XPATH, '//*[@id="select-customer-button"]' )
        cari_onay.click()
        time.sleep(1)

        #faturaya_tikla
        fatura = '//*[@id="sell-detail-div"]/div[2]/div[2]/form/div/div[1]/div[1]/label/span/span'
        click(fatura)
        time.sleep(1)

        randomSatir = randomInt()
        faturaSayisi = 0

        for l in range(5):
            #yeni_satir
            yenisatir_xpath = '//*[@id="lines-add-row"]'
            click(yenisatir_xpath)
        
            # time.sleep(1)

        time.sleep(1)

        #scroll bottom
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        time.sleep(1)
        #bu şekilde tüm xpathleri seçiyor
        stok_kodlari = driver.find_elements(By.XPATH, '//*[@id="myGrid"]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[1]')
        #ilk kaleme odaklanma
        birinci_kalem = driver.find_element(By.XPATH, '//*[@id="myGrid"]/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]/div[1]')
        birinci_kalem.send_keys(Keys.NULL)
        time.sleep(1)

        for stok_kodu in stok_kodlari:
            # stok koduna tıkla
            time.sleep(1.5)
            stok_kodu.click()
            time.sleep(1)
            stokara = '/html/body/span/span/span[1]/input'
            
            try:
                #stok araya tıkla
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, stokara)))
                click(stokara)
                time.sleep(0.8)

            except NoSuchElementException:
                print("Stok ara bölümü bulunamadı.")
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, stokara)))
                click(stokara)
                time.sleep(0.8)    
            
            try:
                sendkeys(stokara, "1")
                time.sleep(0.8)
            except NoSuchElementException:
                print("Stok aranamadı.")
                actions.send_keys(Keys.ESCAPE).perform()
                stok_kodu.click()
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, stokara)))
                click(stokara)
                time.sleep(0.8)
                sendkeys(stokara, "1")
                time.sleep(0.8)
            WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="select2-itemname-select-results"]/li[1]'))
                )
            
            time.sleep(0.1)

            actions.send_keys(Keys.ENTER).perform()
            time.sleep(0.8)

            #fatura kalemine tutar ekle
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.5)
            actions.send_keys(randomInt()).perform()
            time.sleep(0.5)
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.5)
            actions.send_keys(randomInt()).perform()
            time.sleep(0.5)
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.3)
            # actions.perform()
            

        # notlar xpath = //*[@id="notes-totals"]/div/div/div/div[1]
        # not tablosu büyüme = style = resize: vertical; overflow: auto; height: 400px;
        # yeninot = '//*[@id="notes-add-row"]'

        # WebDriverWait(driver, 5).until(
        #     EC.element_to_be_clickable((By.XPATH, yeninot))
        # )

        # for i in range (1):

        #     click(yeninot)

        # notlar_tablo = driver.find_element(By.XPATH, '//*[@id="notes-totals"]/div/div/div/div[1]')
        # driver.execute_script("arguments[0].setAttribute('style', 'resize: vertical; overflow: auto; height: 400px;')", notlar_tablo)
        
        # #not satır xpathleri seçme
        # notlar_xpath = driver.find_elements(By.XPATH, '//*[@id="notes-grid"]/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div')

        # for not1 in notlar_xpath:

        #     actions.double_click(not1)
        #     actions.send_keys("1")
        #     actions.perform()

        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        #kaydete tıkla
        time.sleep(1)

        kaydet = '//*[@id="save-sells-button-bottom"]'
        click(kaydet)
        time.sleep(1)

        #kaydı onayla

        hata_sayisi =[]

        try: 
            kaydet_onay = '/html/body/div[10]/div/div[6]/button[1]'
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, kaydet_onay))
            )
            click(kaydet_onay)
        except TimeoutException as error:
            hata_sayisi.append("1")
            while len(hata_sayisi) > 0:
                birinci_kalem.send_keys(Keys.NULL)

                print ("Bazı kalemler doldurulamadı.")

                for stok_kodu in stok_kodlari:

                    if stok_kodu.text == "12344":
                        pass
                    else:
                        stok_kodu.click()
                
                        #stok araya tıkla
                        stokara = '/html/body/span/span/span[1]/input'
                        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, stokara)))
                        click(stokara)
                        time.sleep(1)

                        sendkeys(stokara, "1")
                        WebDriverWait(driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="select2-itemname-select-results"]/li[1]'))
                        )

                        time.sleep(1)

                        actions.send_keys(Keys.ENTER)
                        time.sleep(0.3)

                        #fatura kalemine tutar ekle
                        actions.send_keys(Keys.TAB)
                        time.sleep(0.3)
                        actions.send_keys(randomFloat())
                        time.sleep(0.3)
                        actions.send_keys(Keys.TAB)
                        time.sleep(0.3)
                        actions.send_keys(randomInt())
                        time.sleep(0.3)
                        actions.send_keys(Keys.TAB)
                        time.sleep(0.3)
                        actions.perform()
                        time.sleep(1)
                hata_sayisi = []
                for kontrol in stok_kodlari:

                    if not "1" in kontrol.text:

                        hata_sayisi.append("1")
                        print ("Bazı Hatalar düzeltilemedi.")

                if len(hata_sayisi) == 0:

                    print("Tüm kalemler dolduruldu.")

            click(kaydet)
            kaydet_onay = '/html/body/div[10]/div/div[6]/button[1]'
            WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, kaydet_onay))
                )
            click(kaydet_onay)

            faturaSayisi += 1

        #onay verdikten sonra yeni alış ekle

        yeni_alis = '/html/body/div[10]/div/div[6]/button[1]' 
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, yeni_alis))
        )
        click(yeni_alis)

        time.sleep(1)

    endTime = datetime.datetime.now()

    print (f"Toplam {faturaSayisi} fatura oluşturuldu.")
    print (f"Başlama zamanı {startTime} \nBitiş zamanı: {endTime}")

satis_fatura_ac = tk.Button(text="Satış faturası açma",command=satislar)
satis_fatura_ac.place(x=100,y=50)

arayuz.mainloop()