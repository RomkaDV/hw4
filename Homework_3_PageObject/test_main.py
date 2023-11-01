from testpage import OperationHelper
import pytest
import logging
import yaml


with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


def test_step2(browsser):
    logging.info("Test 2 Starting")
    testpage = OperationHelper(browsser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("password"))
    testpage.click_login_button()
    assert testpage.get_enter_text() == f"Hello, {testdata.get('login')}"

def test_step3(browsser):
    #  проверка механики работы формы Contact Us
    logging.info("Test 3 Contact_us Starting")
    testpage = OperationHelper(browsser)
    testpage.click_contact_btn()
    testpage.add_your_name(testdata.get("username"))
    testpage.add_your_email(testdata.get("user_email"))
    testpage.add_your_content(testdata.get("content"))
    testpage.click_contact_us_btn()
    assert testpage.get_allert_message() == "Form successfully submitted", "Test FAILED!"


if __name__ == "__main__":
    pytest.main(["-vv"])