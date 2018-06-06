from pages import HomePage, SelectMakePage, SelectModelsPage, SelectCarPage, SelectTrim, ReviewVehiclePage, ReviewDetailsPage, SelectDealerPage
from utility import return_random
from selenium import webdriver
from selenium import webdriver
import time

inventoryflow = True

def inventory_exists() :
    time.sleep(2)
    try:
        driver.find_element_by_xpath("//div[contains(@class,'InventoryList___2RhEw')]")
    except :
        return False
    return True

driver = webdriver.Chrome()
driver.get('https://autogravity.com')
driver.maximize_window()

# Home Page
homepage = HomePage(driver)
homepage.click_button()

# Select Make Page
makepage = SelectMakePage(driver)
makepage.select_random_make()

# Select Model Page
modelpage = SelectModelsPage(driver)
modelpage.select_random_model() 
modelpage.use_location()


if(inventory_exists()) :
    print('Inventory Found!')
    carpage = SelectCarPage(driver)
    carpage.select_random_car()
else :
    inventoryflow = False
    trimpage = SelectTrim(driver)
    trimpage.select_random_trim()

if(inventoryflow):
    reviewvehicle = ReviewVehiclePage(driver)
    reviewvehicle.click_next_button()

reviewdetails = ReviewDetailsPage(driver)
reviewdetails.click_next_button()

if(not inventoryflow):
    dealerpage = SelectDealerPage(driver)
    dealerpage.select_dealer()

time.sleep(5)
driver.close()





