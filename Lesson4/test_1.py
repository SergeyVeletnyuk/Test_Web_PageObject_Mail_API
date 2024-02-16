import time
from testpage import OperationsHelpers
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, send_email):
    logging.info("Test1 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser, send_email):
    logging.info("Test2 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("leonid")
    testpage.enter_pass("142153c067")
    testpage.click_login_button()
    assert testpage.get_user() == "Home"


def test_step3(browser, send_email):
    logging.info("Test3 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("leonid")
    testpage.enter_pass("142153c067")
    testpage.click_login_button()
    testpage.click_new_post_btn()
    time.sleep(testdata['sleep_time'])
    testpage.title_post("Privet")
    testpage.description_post("Super Description")
    testpage.content_post("This is for you")
    time.sleep(testdata['sleep_time'])
    testpage.click_save_post_btn()
    assert testpage.success_save_post() == "This is for you"


def test_step4(browser, send_email):
    logging.info("Test4 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("leonid")
    testpage.enter_pass("142153c067")
    testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.contact_name("Sergey")
    testpage.contact_email("marusya@mail.ru")
    testpage.contact_content("Good job")
    testpage.click_contact_us_btn()
    time.sleep(testdata['sleep_time'])
    assert testpage.contact_alert() == "Form successfully submitted"
