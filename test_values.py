import pytest
from endpoints import EndPoints
from values import Values
import logging
import locale


class TestValuesPage():

    @pytest.yield_fixture(scope="class", autouse=True)
    def setup_teardown_method(driver):
        locale.setlocale(locale.LC_ALL, '')
        self.driver = driver
        self.logging = logging.basicConfig(filename='exersice1.log', filemode='w')
        value_end_point = EndPoints.get("base_end_point")+EndPoints.get("values_end_point")
        driver.get(value_end_point)
        self.values_obj = Values(driver, logging)
        slef.lable_text_dict = self.values.dict_lable_text()
        yield
        driver.close()

    def test_count_of_values(self):
        actual_count = self.values.get_element_count(self.lable_text_dict)
        assert actual_count == 12

    def test_values_of_screen_grater_than_0(self):
        for lable, value in self.lable_text_dict.items():
            str_val = value.text
            assert locale.atof(str_val.strip('$')) > 0

    def test_balance(self):
        lable_txt_dict = self.lable_text_dict
        lable_txt_dict.pop("lbl_ttl_val", None)
        text_list = [locale.atof(val.strip('$')) for val in list(lable_txt_dict.values())]
        total = sum(text_list)
        expected_total = locale.atof((self.lable_text_dict['lbl_ttl_val']).strip('$'))
        assert total == expected_total

    def test_if_currency_formatted(self):
        text_list = list(self.lable_text_dict.values())
        for text_val in text_list:
            actual = text_val
            num_converted = locale.atof(text_val.strip('$'))
            expected = locale.currency(num_converted, grouping=True)
            assert actual == expected
