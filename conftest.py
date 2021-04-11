import pytest
from selenium import webdriver
from endpoints import EndPoints
driver = webdriver.Chrome("/valid/chrome_driver/path")


@pytest.yield_fixture(scope="session", autouse=True)
def setup_teardown_method(driver):
    base_end_point = EndPoints.get("base_end_point")
    driver.get(base_end_point)
    yield
    driver.quit()
