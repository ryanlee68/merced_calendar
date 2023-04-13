from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests
import json

from . import db
from sqlalchemy.orm import Session
from .parser import parse_json
from .tables import Subject
from sqlalchemy import delete

TERM = '202330'

def get_data(cookies: list[dict]) -> list[dict]:
    params = {
        # 'txt_courseReferenceNumber': '33918',
        'txt_term': TERM,
        'startDatepicker': '',
        'endDatepicker': '',
        # you dont need unique session id
        # 'uniqueSessionId': 'fsdfd',
        'uniqueSessionId': '',
        'pageOffset': 0,
        'pageMaxSize': 5000,
        'sortColumn': 'subjectDescription',
        'sortDirection': 'asc',
    }
    s = requests.Session()
    for cookie in cookies:
        cookie.pop('sameSite', None)
        if expires := cookie.pop('expiry', None):
            cookie['expires'] = expires
        if http_only := cookie.pop('httpOnly'):
            cookie['rest'] = {'HttpOnly': http_only}
        s.cookies.set(**cookie)

    x = s.get('https://reg-prod.ec.ucmerced.edu/StudentRegistrationSsb/ssb/searchResults/searchResults', params=params )

    c = 0
    all_data = []
    while(data := x.json()['data']):
        all_data += data
        c+=1
        params['pageOffset'] += 500
        x = s.get('https://reg-prod.ec.ucmerced.edu/StudentRegistrationSsb/ssb/searchResults/searchResults', params=params)
    #     print(f"{params['pageOffset'] = }")
    # print(f"{len(all_data)=}")
    return all_data



def get_cookies() -> list[dict]:
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(executable_path='/Users/ryanlee/Desktop/merced_calendar/react-flask-merced/flask-api/chromedriver.exe')
    driver.get('https://reg-prod.ec.ucmerced.edu/StudentRegistrationSsb/ssb/registration/registration')
    register_for_class_link = driver.find_element('id', 'classSearch')
    register_for_class_link.click()
    dropdown = driver.find_element('id', 's2id_txt_term')
    dropdown.click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, TERM)))
    semester_selection = driver.find_element('id', TERM)
    semester_selection.click()
    dropdown = driver.find_element('id', 'term-go')
    dropdown.click()
    # with open("cookies.json", 'w') as cookies:
    #     json.dump(driver.get_cookies(), cookies, indent=4)

    return driver.get_cookies()

def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        get_data(get_cookies())
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

def grab_db():
    with Session(db.engine) as session:
        session.execute(delete(Subject))
        session.add_all(parse_json(get_data(get_cookies())))
        session.commit()

if __name__ == '__main__':
    # main()
    grab_db()

