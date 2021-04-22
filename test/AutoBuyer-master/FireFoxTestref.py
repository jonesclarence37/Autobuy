import time
from selenium import webdriver
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('https://www.bestbuy.com/site/call-of-duty-black-ops-cold-war-standard-edition-playstation-5/6427993.p?skuId=6427993')
#import pagerduty


class PagePoller:
    def __init__(self, url):
        #self.url = url
        self.createBrowser()
        print("init")
        checkAvailable(self)

        #btn btn-disabled btn-lg btn-block add-to-cart-button

    def checkAvailable(self):
        print(self)
        print(driver)
        addToCartButton = addButton = self.driver.find_element_by_class_name("add-to-cart-button")
        if ("btn-disabled" in addToCartButton.get_attribute("class")):
            print("here")
            return False
        else:
            addToCartButton.click()
            print("Clicked")
            return True

    def createBrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def refreshPage(self):
        self.driver.close()
        self.driver.quit()
        self.createBrowser()


#textFile = open("bestbuy-links1.txt", "r")
textFile = open("/Users/clarencejones/Downloads/AutoBuyer-master/te.txt", "r")
lines = textFile.readlines()
print("Buy now my guy")
print(lines)


pages = []
for u in lines:
    pages.append(u)
    print("Test")

while True:
    toRemove = []
    for p in pages:
        if (p.checkAvailable()):
            #print("Not available")
            #pagerduty.sendPagerDutyAlert()
            toRemove.append(p)
        else:
            print("Not available")
            #print(p)
            p.refreshPage()

    for p in toRemove:
        pages.remove(p)

    time.sleep(0)



#
# #driver = webdriver.Firefox()
#
# # happy case - item is available
# class PagePoller:
#     driver.get("https://www.bestbuy.com/site/call-of-duty-black-ops-cold-war-standard-edition-playstation-5/6427993.p?skuId=6427993")
#     def checkAvailable(self):
#             addToCartButton = addButton = self.driver.find_element_by_class_name("add-to-cart-button")
#             if ("btn-disabled" in addToCartButton.get_attribute("class")):
#                 print("here")
#                 return False
#             else:
#                 addToCartButton.click()
#                 return True
#addToCartButton = addButton = self.driver.find_element_by_class_name("add-to-cart-button")
#addToCartButton.click()
#
#
# #driver.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440")
#


# good
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" style="padding:0 8px">
# </button>


# bad
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" style="padding: 0px 8px;">Sold Out</button>