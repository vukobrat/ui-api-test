import pytest

from src.pages.CareersPage import CareersPage, save_job_data_to_txt
from src.pages.HomePage import HomePage
from tests.ui.common.helpers import get_expected_file_path, load_expected_data


@pytest.mark.ui
def test_career_page(browser):
    home_page = HomePage(browser)
    careers_page = CareersPage(browser)

    home_page.button_careers.click()

    browser.execute_script("arguments[0].scrollIntoView(true);", careers_page.label_current_openings)

    job_count = careers_page.count_job_positions()

    file_path = get_expected_file_path("careers_page_expected_data.yaml")
    expected_data = load_expected_data(file_path)

    assert job_count == expected_data["expected_job_count"]

    job_data = careers_page.get_job_titles_and_locations()
    save_job_data_to_txt(job_data, 'job_results.txt')  # output file can be found at root level after run
