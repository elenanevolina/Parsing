import requests, lxml
from bs4 import BeautifulSoup

def get_bs(url):
	head = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	}
	txt = requests.get(url, headers=head).text
	return BeautifulSoup(txt, 'lxml')

def save_html(url):
    soup = get_txt(url)
    t_body = soup.find('tbody')
    list_tr = t_body.find_all('tr')
    f = open('index.html', 'w', encoding='utf-8')
    f.write(str(list_tr))
    f.close()

def get_list_tr():
    f = open('index.html', 'r')
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    list_tr = soup.find_all('tr')
    f.close()
    return list_tr

def print_results(results):
    f = open('task_2.txt', 'w')
    for line in results:
        line = '%-4d%-26s%-4d%-4d' % (line[0], line[1], line[2], line[3])
        # line = '{0:4d}{1:26s}{2:4d}{3:4d}\n'.format(line[0], line[1], line[2], line[3])
        f.write(line + '\n')
    f.close()