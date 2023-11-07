import yaml
from module import Site
import pytest
import time


with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

def test_create_post(site, selector_button, selector_password, selector_login, create_button, selector_title,
               selector_description, selector_content, save_button, title_post):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", selector_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", selector_button)
    btn.click()
    btn_create = site.find_element("xpath", create_button)
    btn_create.click()
    input3 = site.find_element("xpath", selector_title)
    input3.send_keys(testdata['title'])
    input4 = site.find_element("xpath", selector_description)
    input4.send_keys(testdata['description'])
    input5 = site.find_element("xpath", selector_content)
    input5.send_keys(testdata['content'])
    btn_save = site.find_element("xpath", save_button)
    btn_save.click()

    time.sleep(testdata["sleep_time"])

    title_label = site.find_element("xpath", title_post)
    assert title_label.text == testdata["title"], "Test failed"

if __name__ == "__main__":
    pytest.main(["-vv"])