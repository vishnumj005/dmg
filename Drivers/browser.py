from selenium import webdriver

browser = 'chrome'

if browser == 'chrome':
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver.maximize_window()

elif browser == 'firefox':
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(executable_path=GeckoDriverManager("v0.26.0").install())
    driver.maximize_window()

elif browser == 'edge':
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
    driver.maximize_window()