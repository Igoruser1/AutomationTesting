from base.base_object import BaseObject
from selenium.common.exceptions import NoSuchElementException
from locators.locators_list import IndexPageLocators as ind


class Authorization(BaseObject):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_correct_username(self):
        self.is_visible('id', ind.FIND_USERNAME_FIELD_ID).send_keys('standard_user')
