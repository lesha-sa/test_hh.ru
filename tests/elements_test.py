import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from pages.main_page import FilterJobs


class TestFilterHH:

    def test_advanced_search(self, driver):
        filter_jobs_hh = FilterJobs(driver, 'https://yaroslavl.hh.ru/')
        filter_jobs_hh.open()
        filter_jobs_hh.open_advanced_search()
        filter_jobs_hh.keywords()
        filter_jobs_hh.choice_of_specialization()
        filter_jobs_hh.add_region()
        filter_jobs_hh.choice_education()
        filter_jobs_hh.choice_of_employment_type()
        filter_jobs_hh.choice_schedule()
        filter_jobs_hh.sort_by_data()
        filter_jobs_hh.button_find()
        time.sleep(15)



