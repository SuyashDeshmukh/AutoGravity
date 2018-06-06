from selenium import webdriver
from utility import return_random
import time

class HomePage():
    driver = None
    url = 'https://www.autogravity.com'
    get_started_locator = 'homeButton___3IaYm'
    def __init__(self,driver) :
        self.driver = driver

    def click_button(self):
        started = self.driver.find_element_by_class_name(self.get_started_locator)
        started.click()

class SelectMakePage():
    driver = None
    makes = None
    makes_locator = "div[data-gtm='selectedMake']"

    def __init__(self,driver) :
        time.sleep(2)
        self.driver = driver

    def get_makes(self):
        self.makes = self.driver.find_elements_by_css_selector(self.makes_locator)
    
    def select_random_make(self):
        self.get_makes()
        random_value = return_random(len(self.makes))
        self.makes[random_value].click()

class SelectModelsPage() :
    driver = None
    models = None
    models_locator = "div[data-gtm='selectedModel']"
    location_text_locator = "//div[contains(text(), 'Tell us where you are so we can show you inventory nearby')]"
    my_location_locator = "//span[contains(text(),'USE MY LOCATION')]"

    def __init__(self, driver) :
        time.sleep(2)
        self.driver = driver
    
    def get_models(self) :
        self.models = self.driver.find_elements_by_css_selector(self.models_locator)

    def select_random_model(self):
        self.get_models()
        random_value = return_random(len(self.models))
        self.models[random_value].click()

    def use_location(self):
        if(self.driver.find_elements_by_xpath(self.location_text_locator)) :
            location = self.driver.find_element_by_xpath(self.my_location_locator)
            location.click()
        else :
            pass
    
class SelectCarPage():
    driver = None
    cars = None
    cars_locator = 'inventoryListCard___1My3t'

    def __init__(self, driver) :
        time.sleep(2)
        self.driver = driver

    def get_cars(self) :
        self.cars = self.driver.find_elements_by_class_name(self.cars_locator)
    
    def select_random_car(self):
        self.get_cars()
        random_value = return_random(len(self.cars))
        self.cars[random_value].click()

class SelectTrim():
    driver = None
    trims = None
    trims_locator = 'TrimListItem___2BANQ'

    def __init__(self,driver):
        time.sleep(2)
        self.driver = driver

    def get_trims(self) :
        self.trims = self.driver.find_elements_by_class_name(self.trims_locator)
    
    def select_random_trim(self):
        self.get_trims()
        random_value = return_random(len(self.trims))
        self.trims[random_value].click()

class SelectDealerPage():
    driver = None
    select_dealer_locator = "button[data-gtm='confirmDealer']"

    def __init__(self, driver):
        time.sleep(2)
        self.driver = driver

    def select_dealer(self):
        select_button = self.driver.find_element_by_css_selector(self.select_dealer_locator)
        select_button.click()
    
class ReviewVehiclePage() :
    driver = None
    next_button_locator = 'Button___32Kv9'

    def __init__(self, driver) :
            time.sleep(2)
            self.driver = driver

    def click_next_button(self) :
        next_button =  self.driver.find_element_by_class_name(self.next_button_locator)
        next_button.click()

class ReviewDetailsPage() :
    driver = None
    button_locator = "button[data-gtm='confirmDetails']"

    def __init__(self, driver) :
            time.sleep(2)
            self.driver = driver

    def click_next_button(self) :
        confirm_button =  self.driver.find_element_by_css_selector(self.button_locator)
        confirm_button.click()


