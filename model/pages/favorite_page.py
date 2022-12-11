from selene.support.conditions import have
from selene.support.shared import browser


class FavoritePage:

    def search_and_open_item(self):
        browser.element('.catalog-btn').click()
        browser.element('[class="list-menu-item"][href="/catalog/chai"]').click()
        browser.element('[href = "/catalog/krasnyi-chai"]').click()
        browser.element('[class ="banners-link product-card-new"][href="/product/5581"]').click()
        return self

    def click_to_like_button(self):
        browser.element('.product-links-icon--favourite').click()
        return self

    def delete_from_favorite(self):
        browser.element('.likes-btn').click()
        browser.element('.control--fav').click()
        return self

    def check_favorite_page(self):
        browser.element('.likes-btn').click()()
        browser.element('.product-card-new__title').should(have.text('Чай красный'))
        return self
