from selene.support.conditions import have
from selene.support.shared import browser


class CatalogPage:

    def open_subcatalog(self):
        browser.element('.catalog-btn').click()
        browser.element('[href="/catalog/ovoshhi-i-frukty"]').click()
        return self

    def revision_result(self):
        browser.element('.filter-list-wrapper').should(have.text('Свежие овощи'))
        browser.element('.filter-list-wrapper').should(have.text('Свежие фрукты'))
        browser.element('.filter-list-wrapper').should(have.text('Новинки'))
        browser.element('.filter-list-wrapper').should(have.text('Скидки'))
        browser.element('.filter-list-wrapper').should(have.text('Наша марка'))
        return self
