from selenium import webdriver


driver = webdriver.Chrome()


driver.get(
    "https://example.com/login"
)


driver.find_element(
    "id",
    "old-login-button"
).click()