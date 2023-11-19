from seleniumpagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'button_homepage_logo': ('XPATH', '//a[@class="header--logo"]'),
        'button_agree_cookies': ('XPATH', '//button[contains(text(), "Agree & Continue")]'),
        'button_about_us': ('XPATH', '//span[contains(text(), "About Us ")]'),
        'button_about_us_company': ('XPATH', '//a[contains(text(), "Company")]'),
        'button_careers': ('XPATH', '//a//span[contains(text(), "Careers")]')

    }

