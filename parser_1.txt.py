import datetime
import module6 as m

url = 'https://www.championat.com/football/_england/tournament/4013/table/'
bs = m.get_bs(url)

from datetime import date

current_date = date.today()
print(current_date)

tbody = bs.find('tbody')
list_tr = tbody.find_all('tr')
results = []
for tr in list_tr:
    list_td = tr.find_all('td')
    list_td[1] = list_td[1].find('span', class_= 'table-item__name')
    list_td[2]=list_td[2].find('strong')
    list_td = [td.contents[0] for td in list_td]
    list_td[0] = int(list_td[0].strip())
    list_td[2] = int(list_td[2])
    list_td[3] = int(list_td[3])
    list_td[4] = int(list_td[4])
    list_td[5] = int(list_td[5])
    results.append(list_td)

for item in results:
    f = open('task_1.txt', 'w')
    s = '{:-3d} {:25s}{:-4d}{:-4d}{:-4d}{:-4d}'
    print(s.format(item[0], item[1], item[2], item[3], item[4], item[5]))
    f.close()

m.print_results(results)