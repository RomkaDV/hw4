from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_ENTER_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id = "contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id = "contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_enter_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_ENTER_USER, time=3)
        text = enter_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ENTER_USER[1]}")
        return text

    def click_contact_btn(self):
        logging.info("Click Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def add_your_name(self, name):
        logging.info(f"Send {name} to element {TestSearchLocators.LOCATOR_NAME_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_NAME_FIELD)
        login_field.clear()
        login_field.send_keys(name)

    def add_your_email(self, email):
        logging.info(f"Send {email} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        login_field.clear()
        login_field.send_keys(email)

    def add_your_content(self, content):
        logging.info(f"Send {content} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        login_field.clear()
        login_field.send_keys(content)

    def click_contact_us_btn(self):
        logging.info("Click Contact button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def get_alert_txt(self):
        alert = self.driver.switch_to.alert
        message = alert.text
        alert.accept()
        return message

    def get_allert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        txt = self.get_alert_txt()
        logging.info(f"Alert message is {txt}")
        return txt