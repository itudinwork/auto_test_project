from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
class BasePage():
    def __init__(self, browser, url, timeout=10): #конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): # Он должен открывать нужную страницу в браузере
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"