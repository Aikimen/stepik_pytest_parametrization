link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_basket_button(browser):
    browser.get(link)
    # находим кнопку по уникальному локатору
    button = browser.find_element_by_css_selector('button.btn-add-to-basket')
    # получаем значение атрибута "type", присутствующего в описании элемента "button"
    # возвращается строка, содержащаяся в "type='submit'"
    button_type = button.get_attribute('type')
    print("value of button type: ", button_type)
    # если уникальное значение type, содержащееся в элементе button
    # присутствует и равно "submit" (что задано по умолчанию)
    # то assert проходит тест "pass" и показывает присутствие элемента
    # на странице
    assert button_type == 'submit', f'Кнопка не найдена'
