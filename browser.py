from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:

    def __init__(self):
        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # OBLIGATORIU PENTRU ORANGEHRM ÎN CLOUD:
        # 1. Forțăm un User-Agent real de calculator pentru a activa JavaScript în mod headless
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # 2. Ignoră eventualele erori de certificat SSL de pe server
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--allow-running-insecure-content")

        self.driver = webdriver.Chrome(options=chrome_options)

        # Rămâne comentat sau șters
        # self.driver.maximize_window() 
        
        # Opțional: Dacă serverul GitHub se mișcă mai greu, mărește timpul la 10 secunde
        self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()
