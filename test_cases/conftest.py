from selenium import webdriver
import pytest

import pytest
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    # if request.param == "firefox":
    #     web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()

