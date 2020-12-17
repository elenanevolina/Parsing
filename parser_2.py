import module as m
from datetime import datetime

url = 'https://www.championat.com/football/_england/tournament/4013/table/'
bs = m.get_bs(url)

current_datetime = datetime.now().date()
print(current_datetime)

tbody = bs.find('tbody')
list_tr = tbody.find_all('tr')

results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    order = int(list_td[0].contents[0].strip())
    name = list_td[1].find('span', class_='table-item__name').contents[0]
    balls = list_td[6].find_all('span')
    ball_z = int(balls[0].contents[0])  # забитых
    ball_p = int(balls[2].contents[0])  # пропущенных
    rec = [order, name, ball_z, ball_p]
    results.append(rec)

m.print_results(results)

