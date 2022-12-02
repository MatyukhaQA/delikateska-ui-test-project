
import allure

from model.pages.web_delikateska import open_url, authorization, view_account, search_value, check_search_result, \
    open_subcatalog, revision_result, search_and_open_item, add_to_favorite, favorite_page, search_ingridients, \
    check_recipe


@allure.tag('web')
def test_login_possitive():
    open_url()
    with allure.step('Заполняем информацию для входа'):
        authorization()
    with allure.step('Переходим на страницу пользователя'):
        view_account()


@allure.tag('web')
def test_search_item():
    open_url()
    with allure.step('Ищем товар'):
        search_value('Тунец')
    with allure.step('Проверяем результат поиска'):
        check_search_result()


@allure.tag('web')
def test_view_catalog():
    open_url()
    with allure.step('Открываем подкаталог "Овощи и фрукты"'):
        open_subcatalog()
    with allure.step('Проверяем страницу'):
        revision_result()


@allure.tag('web')
def test_add_to_favorite():
    open_url()
    with allure.step('Заполняем информацию для входа'):
        authorization()
    with allure.step('Ищем любимый товар'):
        search_and_open_item()
    with allure.step('Добавляем товар в избранное'):
        add_to_favorite()
    with allure.step('Проверяем, что товар присутствует в избранных'):
        favorite_page()


@allure.tag('web')
def test_search_recipe():
    open_url()
    with allure.step('Ищем ингредиент'):
        search_ingridients()
    with allure.step('Проверяем наличие нужных рецептов'):
        check_recipe()
