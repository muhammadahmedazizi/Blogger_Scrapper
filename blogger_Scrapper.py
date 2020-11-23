from bs4 import BeautifulSoup
import requests
import urllib3

url = 'http://ranaii-e-khayal.blogspot.com/2020/11/%20%20%20%20%20%20%20.html'

blog_url = 'http://ranaii-e-khayal.blogspot.com'


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







def post_scrapper (url):
    page = requests.get(url)
    data = page.text
    page.close()

    soup = BeautifulSoup(data, 'lxml')

    for post in soup.find_all('div', class_='post'):
        title = post.find('h3', class_='post-title')
        body = post.find('div', class_='post-body')
        date = post.find('abbr', class_='published')

        labels = post.find('span', class_='post-labels').text
        labels = labels.split(':')
        labels = labels[1]
        labels = labels.split(',')
        new_labels = list(map(str.strip, labels))

        print (title)
        print (body)
        print(new_labels)
        print (date)

#blog_scrapper(url)

#links_extractor(blog_url)
print (extract_post_links(page_links_extractor(blog_url)))

#p_links = ['http://ranaii-e-khayal.blogspot.com/search?updated-max=2009-10-17T12:01:00%2B06:00&max-results=12&reverse-paginate=true','http://ranaii-e-khayal.blogspot.com/search?updated-max=2009-07-15T13:08:00%2B06:00&max-results=12&start=373&by-date=false']

#print(extract_post_links(p_links))