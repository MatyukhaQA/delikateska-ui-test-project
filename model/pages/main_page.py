import os

from dotenv import load_dotenv
from selene.support.conditions import have
from selene.support.shared import browser

load_dotenv()

LOGIN = os.getenv('login')
PASSWORD = os.getenv('password')
URL = os.getenv('url')


class MainPage:

    def open_url(self):
        browser.open(URL)
        return self

    def authorization(self):
        browser.element('.login-btn').click()
        browser.element('[name="email-pass"]').type(LOGIN).press_enter()
        browser.element('[type="password"]').type(PASSWORD).press_enter()
        return self

    def view_account(self):
        browser.element('.header-avatar').click()
        browser.element('.container-personal-account').should(have.text('Активные заказы'))
        return self

    def delete_subscribe_window(self):
        browser.element('#onesignal-slidedown-cancel-button').click()
