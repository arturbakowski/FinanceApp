from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url)

    def tearDown(self):
        self.browser.quit()


    def test_incomes(self):

    # User goes to "Incomes" menu
        self.browser.find_element_by_link_text("Incomes").click()
    # User inputs monthly incomes
    # User sees entered monthly incomes
    # User deletes a wrong record

    def test_expenses(self):
    # User goes to "Expenses" menu
        self.browser.find_element_by_link_text("Expenses").click()
    # User inputs monthly expenses
    # User sees entered montly expenses
    # User deletes a wrong record

    def test_analysis(self):
    # User goes to "Analysis" menu
        self.browser.find_element_by_link_text("Analysis").click()
    # User choice period to analyse budget
    # User sees incomes, expenses and special graphs and charts

    def test_savings(self):
    # User goes to "Savings" menu
        self.browser.find_element_by_link_text("Savings").click()
    # User inputs montly savings
    # User sees entered monthly savings
    # User deletes a wrong record


if __name__ == '__main__':
    unittest.main()

