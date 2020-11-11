# stepik_pytest_parametrization
Выполнение задания: запуск автотестов для разных языков интерфейса на курсе "Selenium + Python: автоматизация" от Степик.
Task completion: run autotests for different interface languages on the course "Selenium + Python: automation" from Stepik. org

A solution that allows you to run autotests for different user languages by passing the desired language on the command line.

File conftest.py contains a handler that reads the language parameter from the command line.
Implemented in a file conftest.py logic for launching the browser with the specified user language. The browser is declared in the browser fixture and passed to the test as a parameter.
To file "test_items.py" a test that checks that the product page on the site contains an add to cart button.
For example, a product that is available at http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
The test is run with the language parameter with the following command:
py test --language=es test_items.py # you can use any other locale instead of es
and it is successful.
The code can work for the Chrome browser and for Firefox.
