from pages import HomePage, SelectMakePage, SelectModelsPage, SelectCarPage, SelectTrim, ReviewVehiclePage, ReviewDetailsPage, SelectDealerPage
from utility import return_random
from selenium import webdriver
import time

class Test():
    inventoryflow = True
    no_dealers = False
    driver = None
    url = 'https://autogravity.com'

    def inventory_exists(self) :
        time.sleep(2)
        try:
            self.driver.find_element_by_xpath("//div[contains(@class,'InventoryList___2RhEw')]")
        except :
            return False
        return True

    def setup(self):
        self.driver = webdriver.Chrome() 
        self.driver.get(self.url)
        self.driver.maximize_window()

    def teardown(self):
        print('Automation Process complete')
        time.sleep(5)
        self.driver.close()

    def main(self):
        # Setup the driver and url
        self.setup()

        # Home Page
        homepage = HomePage(self.driver)
        homepage.click_button()

        # Select Make Page
        makepage = SelectMakePage(self.driver)
        makepage.select_random_make()
        
        # Select Model Page
        modelpage = SelectModelsPage(self.driver)
        modelpage.select_random_model() 
        modelpage.use_location()

        # Check for flow type
        if(self.inventory_exists()) :
            carpage = SelectCarPage(self.driver)
            carpage.select_random_car()
        else :
            self.inventoryflow = False
            trimpage = SelectTrim(self.driver)
            trimpage.select_random_trim()

        if(self.inventoryflow):
            reviewvehicle = ReviewVehiclePage(self.driver)
            reviewvehicle.click_next_button()

        # Review Details Page
        reviewdetails = ReviewDetailsPage(self.driver)
        reviewdetails.click_next_button()

        if(not self.inventoryflow):
            dealerpage = SelectDealerPage(self.driver)
            dealerpage.select_dealer()

        # Close driver
        self.teardown()


if( __name__ == '__main__'):
    test = Test()
    test.main()



