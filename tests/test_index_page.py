from pom.index_page import Authorization
import pytest
import random

random_nambers = [1,2,3]

@pytest.mark.ui
def test_1():
    assert 1 == random.choice(random_nambers)

@pytest.mark.usefixtures('setup')
class TestAuthorization:

    @pytest.mark.smoke
    def test_successful_login(self):
        driver = self.driver
        step = Authorization(driver)
        step.enter_correct_username()


