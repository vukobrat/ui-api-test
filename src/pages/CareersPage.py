from selenium.webdriver.common.by import By
from seleniumpagefactory import PageFactory


def save_job_data_to_txt(job_data, file_path='job_results.txt'):
    with open(file_path, 'w') as file:
        for job_entry in job_data:
            file.write(job_entry + '\n')


class CareersPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'label_current_openings': ('XPATH', '//h3[@class="currentOpenings--title"]'),
        'button_all_locations': ('XPATH', '//span[contains(text(), "All Locations")]'),
        'label_position': ('XPATH', '//ul[@class="currentOpenings--jobs"]')

    }

    def count_job_positions(self):
        return len(self.label_position.find_elements(By.TAG_NAME, 'li'))

    def get_jobs(self):
        return self.label_position.find_elements(By.TAG_NAME, 'li')

    def get_job_titles_and_locations(self):
        jobs_list = self.get_jobs()
        job_data = []
        for job in jobs_list:
            job_text = job.text.split("\n")
            if len(job_text) > 2:
                title = job_text[1]
                location = job_text[2]
            else:
                title = job_text[0]
                location = job_text[1]
            job_data.append(f"{title}, {location}")
        return job_data

