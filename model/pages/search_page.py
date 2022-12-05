from selene.support.conditions import have
from selene.support.shared import browser


class SearchPage:

    def search_value(self, item):
        browser.element('#search-input').type(item).press_enter()
        return self

    def check_search_result(self, item):
        browser.element('.wrap-header ').should(have.text(f"Результаты по запросу «{item}»"))
        browser.element('.CatalogContainer').should(have.text(item))
        return self

    def search_ingridients(self):
        browser.element('.header-nav__list li:nth-child(3)').click()
        browser.element('[placeholder = "Поиск по рецептам"]').type('Тунец')
        return self

    def check_recipe(self):
        browser.element('.RecipeCard:nth-child(2)').should(have.text('Морепродукты'))
        browser.element('.RecipeCard:nth-child(3)').should(have.text('Рыба'))
        browser.element('.RecipeCard:nth-child(2)').should(have.text('Тунец с творожным кремом'))
        return self
