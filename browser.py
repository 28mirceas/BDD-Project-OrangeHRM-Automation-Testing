from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Browser:

    def __init__(self):

        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # 1. Adaugă această linie pentru a seta o rezoluție stabilă de monitor virtual
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        
        # 2. Pune un caracter '#' la începutul liniei de mai jos pentru a o comenta
        #self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def close(self):
        self.driver.quit()
