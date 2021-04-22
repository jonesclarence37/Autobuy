import time
from selenium import webdriver
fp = webdriver.FirefoxProfile('/Users/clarencejones/desktop/BBB')

driver = webdriver.Firefox(fp)

#import pagerduty


class PagePoller:
    def __init__(self, url):
        self.url = url
        self.createBrowser()

    def GoToCart(self):
        GoToCartButton = GoButton = self.driver.find_element_by_class_name("btn-secondary")
        #if ("btn-disabled" in addToCartButton.get_attribute("class")):
        #    return False
        #else:
        GoToCartButton.click()
        return True

    def checkAvailable(self):
        driver.set_page_load_timeout(3)
        addToCartButton = self.driver.find_element_by_class_name("add-to-cart")
        print("Is it good?")
        print(addToCartButton)
        #driver.set_page_load_timeout(3)
        if ("disabled" in addToCartButton.get_attribute("disabled")):
            print(addToCartButton)
            return False
        else:
            addToCartButton.click()
            driver.set_page_load_timeout(1)
            #self.driver.get("https://www.bestbuy.com/cart")
           # CheckoutButton = self.driver.find_element_by_class_name("checkout-buttons__checkout")
            #CheckoutButton.click()
            #AgeButton = self.driver.find_element_by_class_name("age-verification__button")
            #AgeButton.click()
            return True

    def createBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def refreshPage(self):
        self.driver.close()
        self.driver.quit()
        self.createBrowser()

    def GoToCart(self):
        GoToCartButton = self.driver.find_element_by_class_name("btn-secondary")
        #if ("btn-disabled" in addToCartButton.get_attribute("class")):
        #    return False
        #else:
        GoToCartButton.click()
        return True


textFile = open("/Users/clarencejones/Downloads/AutoBuyer-master/Gamestop.txt", "r")
lines = textFile.readlines()
#print(lines)

pages = []
for u in lines:
    pages.append(PagePoller(u))

while True:
    toRemove = []
    for p in pages:
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
