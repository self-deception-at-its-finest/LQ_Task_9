from playwright.sync_api import expect
from pages.header_component import HeaderComponent
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import random
import allure
import pytest



def test_adding_products_in_cart(page, base_url):
    home_page = HomePage(page)
    header = HeaderComponent(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    with allure.step("Launch browser and Navigate to the website"):
        home_page.open()
        expect(page).to_have_url(base_url + "/")

    with allure.step("Verify that home page is visible successfully"):
        home_page.verify_home_page_visible()

    with allure.step("Click 'Products' button"):
        header.products_button.click()

    with allure.step("Hover over first product and click 'Add to cart'"):
        list_of_added_products = []
        total_price_of_added_products = 0
        i = random.randint(2,10)
        while i > 0:
            result = products_page.add_random_product_in_cart()
            product_name = result["product_name"].replace('\xa0', ' ')
            if product_name in list_of_added_products:
                continue
            list_of_added_products.append(product_name)
            total_price_of_added_products += result["product_price"]
            i += -1
        header.cart_button.click()

    with allure.step("Verify products names added before are similar to those in Cart"):
        items = cart_page.items_description_in_cart_list
        list_of_products_in_cart = []
        for i in range(items.count()):
            list_of_products_in_cart.append(items.nth(i).inner_text().replace('\xa0', ' ').strip())
        assert list_of_added_products == list_of_products_in_cart

    with allure.step("Verify total products price added before is similar to total price in Cart"):
        prices = cart_page.items_price_in_cart_list
        total_price_in_cart = 0
        for i in range(prices.count()):
            total_price_in_cart += int(prices.nth(i).inner_text().split()[1])
        assert total_price_of_added_products == total_price_in_cart



