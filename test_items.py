from time import sleep


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_item_to_basket(browser):
    browser.get(link)
    sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'Кнопка добавления в корзину отсутствует'