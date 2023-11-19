import pytest

from src.pages.CompanyPage import CompanyPage
from src.pages.HomePage import HomePage
from tests.ui.common.helpers import get_expected_file_path, load_expected_data


@pytest.mark.ui
def test_company_page(browser):
    home_page = HomePage(browser)
    company_page = CompanyPage(browser)

    home_page.button_about_us.click()
    home_page.button_about_us_company.click()

    file_path = get_expected_file_path("company_page_expected_data.yaml")
    expected_data = load_expected_data(file_path)

    # HQ, Founded, Size
    assert company_page.label_hq.text == expected_data["HQ"]
    assert company_page.label_founded.text == expected_data["Founded"]
    assert company_page.label_size.text == expected_data["Size"]

    # Consulting Offices
    for office in expected_data["Consulting_Offices"]:
        actual_office = company_page.get_consulting_office(office)
        assert actual_office.text == office

    # Engineering Hubs
    for hub in expected_data["Engineering_Hubs"]:
        actual_hub = company_page.get_engineering_hub(hub)
        assert actual_hub.text == hub

    # Clients
    assert company_page.label_clients.text == expected_data["Clients"]

    # Certifications
    for certification in expected_data["Certifications"]:
        actual_certification = company_page.get_certification_status(certification)
        assert actual_certification.text == certification

    assert browser.current_url == expected_data["Url"]
