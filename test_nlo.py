import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from time import sleep

responce = 'Correct!'

def answer():
    m = math.log(int(time.time()))
    return m

@pytest.fixture(scope="function")
def browserF():
    print('\nstart browser for test..')
    browserF = webdriver.Firefox()
    yield browserF
    print('\nquit browser')
    browserF.quit()

def browser():
    print('\nstart browser for test..')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser')
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browserF, url):
    link = 'https://stepic.org/lesson/{}/step/1'.format(url)
#    sleep(10)
#    browser.implicitly_wait(2)
    browserF.get(link)
    browserF.implicitly_wait(5)
#    browser.find_element(By.XPATH, '//div[@data-state = "no_submission"]').send_keys(str(answer()))
    browserF.find_element_by_xpath('//textarea[@class = "textarea string-quiz__textarea ember-text-area ember-view"]').send_keys(str(answer()))
    browserF.find_element_by_xpath('//button[@class = "submit-submission"]').click()
    assert browserF.find_element_by_xpath('//pre[@class = "smart-hints__hint"]').text == responce, 'Некорректный текст в ответе'
