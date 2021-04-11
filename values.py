class Values():
    def __init__(self, driver, logger):
        self.driver = driver
        self.lbl_id_txt_id_dict = {}
        for i in range(1, 6):
            lbl = f"lbl_val_{str(i)}"
            txt = f"txt_val_{str(i)}"
            self.lbl_txt_id_dict[lbl] = txt
        self.lbl_id_txt_id_dict["lbl_ttl_val"] = "txt_ttl_val"
        self.logging = logger

    def dict_lable_text(self, id_val_text=None):
        # @ params id_val_text : dict with key:value id and value:text id
        # @ return value dict with webdriver elements of keys and values of given ids
        # @ rtype dict

        if not id_val_text:
            id_val_text = self.lbl_id_txt_id_dict
        element_value_text = {}
        for value_id, text_id in id_val_text:
            element_value = self.driver.find_element_by_id(value_id)
            element_text = self.driver.find_element_by_id(text_id)
            element_value_text[element_value] = element_text
        return element_value_text

    def get_element_count(self, element_value_text):
        # @param element_value_text dict with key:element of lable value:element of text
        # @return number of elements visible in the page
        # @rtype number

        count = 0
        for key, val in element_value_text.items():
            try:
                key.is_displayed()
                count = count+1
                val.is_displayed()
                count = count+1
            except StaleElementReferenceException:
                self.logging.info("Element not found")
        return count
