import time
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 #driver = webdriver.Chrome('/Users/clarencejones/Downloads/chromedriver')
fp = webdriver.FirefoxProfile('/Users/clarencejones/desktop/BBB')
driver = webdriver.Firefox(fp)
#driver = webdriver.Chrome(ChromeDriverManager(version="90.0.4430.24").install())
#driver.get("https://www.google.com")




#import pagerduty


class PagePoller:
    def __init__(self, url):
        self.url = url
        self.createBrowser()




    def checkAvailable(self):

        driver.set_page_load_timeout(1)
        addToCartButton = self.driver.find_element_by_class_name("add-to-cart")
        print(addToCartButton.click())
        print("Test1")

        if (addToCartButton.get_attribute("disabled")):
            print("Test2")
            return False
        else:
            addToCartButton.click()
        #try:

        # if (addToCartButton):
        #     print(addToCartButton)
        #     driver.get("https://www.gamestop.com/checkout/?stage=shipping#shipping")
        # else:
        #     print("No item")
        #except TimeoutException:
            email = driver.find_element_by_class_name("form-control email")
            email.sendKeys("Test@test.com")
            return True



    def createBrowser(self):
        self.driver = driver
        self.driver.get(self.url)

        #self.driver = webdriver.Chrome(ChromeDriverManager(version="90.0.4430.24").install())
        # self.driver.get("https://www.gamestop.com/checkout/?stage=shipping#shipping")



    def refreshPage(self):
        #PoolManager().connection_from_url('http://en.wikipedia.org/wiki/Main_Page')
        self.driver.quit()
        self.driver.close()
        #self.driver.quit()
        self.createBrowser()




textFile = open("/Users/clarencejones/Downloads/AutoBuyer-master/Gamestop.txt", "r")
lines = textFile.readlines()
print(lines)

pages = []
for u in lines:
    pages.append(PagePoller(u))

while True:
    toRemove = []
    for p in pages:
        print(p.checkAvailable())
        if (p.checkAvailable()):
            #print("Not available")
            #pagerduty.sendPagerDutyAlert()
            toRemove.append(p)
        else:
            print("Not available")
            p.refreshPage()

    for p in toRemove:
        pages.remove(p)

    #time.sleep(0)



#
# #driver = webdriver.Firefox()
#
# # happy case - item is available
# #driver.get("https://www.bestbuy.com/site/nvidia-titan-rtx-24gb-gddr6-pci-express-3-0-graphics-card/6320585.p?skuId=6320585")
#
#
# #driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#


# good
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" style="padding:0 8px">
# </button>


# bad
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" style="padding: 0px 8px;">Sold Out</button>