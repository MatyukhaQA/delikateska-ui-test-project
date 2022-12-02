import os

from dotenv import load_dotenv
from selene.support.conditions import have
from selene.support.shared import browser

load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
URL = os.getenv('URL')


def open_url():
    browser.open(URL)


def authorization():
    browser.element('.login-btn').click()
    browser.element('[name="email-pass"]').type(LOGIN).press_enter()
    browser.element('[type="password"]').type(PASSWORD).press_enter()


def view_account():
    browser.element('.header-avatar').click()
    browser.element('.container-personal-account').should(have.text('Активные заказы'))


def search_value():
    browser.element('#search-input').type('Тунец').press_enter()


def check_search_result():
    browser.element('.wrap-header ').should(have.text('Результаты по запросу Тунец /'
                                                      'Найдено 16 товаров'))
    browser.element('.CatalogContainer').should(have.text('Тунец'))


def open_subcatalog():
    browser.element('.catalog-btn').click()
    browser.element('[href="/catalog/ovoshhi-i-frukty"]').click()


def revision_result():
    browser.element('[href="/catalog/ovoshhi-i-frukty/r/newbee/yes"]').should(have.text('Новинки'))
    browser.element('[href="/catalog/ovoshhi-i-frukty/r/promo/yes"]').should(have.text('Скидки'))
    browser.element('[href="/catalog/ovoshhi-i-frukty/r/delikateska/yes"]').should(have.text('Наша марка'))


def search_and_open_item():
    browser.element('.catalog-btn').click()
    browser.element('[class="list-menu-item"][href="/catalog/chai"]').click()
    browser.element('[href = "/catalog/krasnyi-chai"]').click()
    browser.element('[class ="banners-link product-card-new"][href="/product/5581"]').click()


def add_to_favorite():
    browser.element('.product-links-icon--favourite').click()


def favorite_page():
    browser.element('.likes-btn').double_click()()
    browser.element('.product-card-new__title').should(have.text('Чай красный'))


def search_ingridients():
    browser.element('.header-nav__list li:nth-child(3)').click()
    browser.element('[placeholder = "Поиск по рецептам"]').type('Тунец')


def check_recipe():
    browser.element('.RecipeCard:nth-child(2)').should(have.text('Морепродукты'))
    browser.element('.RecipeCard:nth-child(3)').should(have.text('Рыба'))
    browser.element('.RecipeCard:nth-child(2)').should(have.text('Тунец с творожным кремом'))
