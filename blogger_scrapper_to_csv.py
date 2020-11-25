from bs4 import BeautifulSoup
import requests
from write_csv import write_csv

import csv
import urllib3

url = 'http://ranaii-e-khayal.blogspot.com/2020/11/%20%20%20%20%20%20%20.html'

blog_url = 'http://tabishain.blogspot.com'

# Forming FileName
file_name = blog_url
file_name = file_name.replace('.blogspot.com','')
file_name = file_name.split('//')
file_name = file_name[-1]
txt_file_name = "Output_Direcotry/"+file_name+".txt"
csv_file_name = "Output_Direcotry/"+file_name+".csv"


over_all_post_lins = []
def extract_post_links (blog_url_list):
    for page_link in blog_url_list:
        page_source = requests.get(page_link)
        page_data = page_source.text
        page_source.close()

        soup = BeautifulSoup(page_data, 'lxml')

        for links in soup.find_all('h3', class_='post-title'):
            link = links.find('a')['href']
            over_all_post_lins.append(link)
    return over_all_post_lins




page_links_list = []
def page_links_extractor(blog_url):
    page_source = requests.get(blog_url)
    page_data = page_source.text
    page_source.close()

    soup = BeautifulSoup(page_data, 'lxml')

    if blog_url not in page_links_list:
        page_links_list.append(blog_url)

    for next_page in soup.find_all('span', id='blog-pager-older-link'):
        if not next_page:
            return (page_links_list)
        else:
            next_page_link = next_page.find('a')['href']

            page_links_list.append(next_page_link)
            page_links_extractor(page_links_list[-1])
    return (page_links_list)





def post_scrapper (urls):
    for url in urls:
        page = requests.get(url)
        data = page.text
        page.close()

        soup = BeautifulSoup(data, 'html.parser')

        for post in soup.find_all('div', class_='post'):
            title = post.find('h3', class_='post-title')
            title= title.get_text(separator='\n')

            body = post.find('div', class_='post-body')
            body = body.get_text(separator='\n')

            date = post.find('abbr', class_='published')
            date = date.get_text(separator='\n')

            if post.find('span', class_='post-labels'):
                labels = post.find('span', class_='post-labels').text
                labels = labels.split(':')
                if len(labels) > 1:
                    labels = labels[1]
                    labels = labels.replace('\n',' ')
                else:
                    labels = ''
            else:
                labels = ''

            # args_list_for_csv = []
            # args_list_for_csv.append(title+'\n')
            # args_list_for_csv.append(body+'\n')
            # args_list_for_csv.append(date+'\n')
            # args_list_for_csv.append(labels+'\n')

            #print(title, body, date, labels)
            try:
                write_csv(title, body, date, labels)
            except:
                print ('error')





#new_list = ["http://ranaii-e-khayal.blogspot.com/2020/11/%20%20%20%20%20%20%20.html"]




#blog_scrapper(url)

#links_extractor(blog_url)
#links_of_posts = extract_post_links(page_links_extractor(blog_url))

#short_links = ['http://ranaii-e-khayal.blogspot.com/search?updated-max=2009-10-17T12:01:00%2B06:00&max-results=12&reverse-paginate=true','http://ranaii-e-khayal.blogspot.com/search?updated-max=2009-07-15T13:08:00%2B06:00&max-results=12&start=373&by-date=false']

post_scrapper(['http://tabishain.blogspot.com'])
#print(extract_post_links())

#'http://anqasha.blogspot.com/'