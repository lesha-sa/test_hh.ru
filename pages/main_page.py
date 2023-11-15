from locators.elements_page_locators import HeadHunterLocators
from pages.base_page import BasePage


class FilterJobs(BasePage):
    locators = HeadHunterLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def open_advanced_search(self):
        self.element_is_visible(self.locators.BUTTON_ADVANCED_SEARCH).click()  #Open advanced search

    def keywords(self):
        self.element_is_visible(self.locators.KEYWORDS).send_keys('Qa automation engineer')   #Input Keywords
        self.element_is_visible(self.locators.KEYWORDS_CHOOSE).click()  #keyword selection


    def choice_of_specialization(self):
        self.element_is_visible(self.locators.BUTTON_SPECIALIZATION).click()
        self.element_is_visible(self.locators.LIST_SPECIALIZATION).click()
        self.element_is_visible(self.locators.LIST_SPECIALIZATION_FIND_TESTER).send_keys('тестировщик')
        self.element_is_visible(self.locators.LIST_SPECIALIZATION_CHOOSE_TESTER).click()
        self.element_is_visible(self.locators.LIST_SPECIALIZATION_BUTTON_ACCEPT).click()


    def add_region(self):
        self.element_is_visible(self.locators.REGION).send_keys("Москва")


    def choice_education(self):
        self.element_is_visible(self.locators.EDUCATION).click()


    def choice_of_employment_type(self):
        self.go_to_element(self.locators.EMPLOYMENT_TYPE).click()


    def choice_schedule(self):
        self.element_is_visible(self.locators.SCHEDULE_FULL_DAY).click()
        self.element_is_visible(self.locators.SCHEDULE_DISTANT_WORK).click()

    def sort_by_data(self):
        self.go_to_element(self.locators.SORT_BY_DATA).click()

    def button_find(self):
        self.element_is_visible(self.locators.BUTTON_FIND).click()