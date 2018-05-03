from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'

conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode('utf8')

cafef_file = open('cafef.html', 'w')
cafef_file.write(text)
cafef_file.close()

soup = BeautifulSoup(text, 'html.parser')
table = soup.find('table', id='tableContent')
tr_list = table.find_all('tr')
# print(tr_list[0].prettify())

item_list = []

for tr in tr_list:
    td_list = tr.find_all('td', 'b_r_c')
    for td in td_list:
        criteria = td.string
        q4_2016 = td.string
        q1_2017 = td.string
        q2_2017 = td.string
        q3_2017 = td.string
        item = {
            'Chỉ tiêu': criteria,
            'Quý 4-2016': q4_2016,
            'Quý 1-2017': q1_2017,
            'Quý 2-2017': q2_2017,
            'Quý 3-2017': q3_2017
        }
        item_list.append(item)

pyexcel.save_as(records=item_list, dest_file_name="BCTC VNM.xlsx")
