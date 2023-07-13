from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are unfamiliar with')
unfamilar_skill = input('>')
print(f'Filtering out {unfamilar_skill}')


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.strip()
        if 'few' in published_date:
            componay_name = job.find(
                'h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.strip()
            if unfamilar_skill not in skills:
                more_info = job.header.h2.a['href']

                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {componay_name}\n')
                    f.write(f'Required Skills: {skills}\n')
                    f.write(f'More Info: {more_info}\n')
                    print(f'File saved: {index}\n')
                print()


if __name__ == '__main__':
    while True:
        find_jobs()
        wait_time_in_mins = 10
        print(f'Waiting {wait_time_in_mins} minutes...')
        time.sleep(wait_time_in_mins * 60)
