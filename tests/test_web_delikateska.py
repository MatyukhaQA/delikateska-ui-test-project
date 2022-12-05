import allure

from model.application_manager import main_page, search_page, favorite_page, catalog_page


@allure.tag('web')
def test_login_positive():
    main_page.open_url()
    with allure.step('Удаляем окно с подпиской'):
        main_page.delete_subscribe_window()
    with allure.step('Заполняем информацию для входа'):
        main_page.authorization()
    with allure.step('Переходим на страницу пользователя'):
        main_page.view_account()


@allure.tag('web')
def test_search_item():
    main_page.open_url()
    with allure.step('Ищем товар'):
        search_page.search_value('Тунец')
    with allure.step('Проверяем результат поиска'):
        search_page.check_search_result('Тунец')


@allure.tag('web')
def test_view_catalog():
    main_page.open_url()
    with allure.step('Открываем подкаталог "Овощи и фрукты"'):
        catalog_page.open_subcatalog()
    with allure.step('Проверяем страницу'):
        catalog_page.revision_result()


@allure.tag('web')
def test_add_to_favorite():
    main_page.open_url()
    with allure.step('Заполняем информацию для входа'):
        main_page.authorization()
    with allure.step('Ищем любимый товар'):
        favorite_page.search_and_open_item()
    with allure.step('Добавляем товар в избранное'):
        favorite_page.add_to_favorite()
    with allure.step('Удаляем окно с подпиской'):
        main_page.delete_subscribe_window()
    with allure.step('Проверяем, что товар присутствует в избранных'):
        favorite_page.check_favorite_page()


@allure.tag('web')
def test_delete_from_favorite():
    main_page.open_url()
    with allure.step('Заполняем информацию для входа'):
        main_page.authorization()
    with allure.step('Удаляем товар из избранного'):
        favorite_page.delete_from_favorite()


@allure.tag('web')
def test_search_recipe():
    main_page.open_url()
    with allure.step('Ищем ингредиент'):
        search_page.search_ingridients()
    with allure.step('Проверяем наличие нужных рецептов'):
        search_page.check_recipe()
