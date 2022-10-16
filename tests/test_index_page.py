from pom.index_page import Authorization
import pytest
import random
import allure

random_nambers = [1,2,3]

@pytest.mark.ui
def test_1():
    assert 1 == random.choice(random_nambers)

@allure.story("тесты про авторизацию")
@pytest.mark.usefixtures('setup')
class TestAuthorization:

    @allure.label("owner","Igor")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("проверка входа в систему")
    @pytest.mark.smoke
    def test_successful_login(self):
        driver = self.driver
        step = Authorization(driver)
        with allure.step("шаг1"):
            step.enter_correct_username()
        with allure.step("шаг2"):
            step.enter_correct_password()
        with allure.step("шаг3"):
            step.clik_login_button()









