from bs4 import BeautifulSoup

html = '''<div style="display:block; margin:0 auto; margin-top:15px; margin-bottom:20px">
	<a class="label label-warning labelMy" href="/korotkie-anekdoty">короткие</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/evrei">про евреев</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/vovochka">про Вовочку</a>				
	<a class="label label-warning labelMy" href="/anekdoty-pro/russkie">про русских</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/shtirlic">про Штирлица</a>			
	<a class="label label-warning labelMy" href="/anekdoty-pro/muzhik">про мужика</a>			
	<a class="label label-warning labelMy" href="/anekdoty-pro/чебурашка">про Чебурашку</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/medved">про медведя</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/nemcy">про немцев</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/chapaev">про Чапаева</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/russkiy-nemec">про русского и немца</a>
	<a class="label label-warning labelMy" href="/anekdoty-pro/жена">про жену</a>
</div>'''

suop = BeautifulSoup(html, features='lxml')
a_tags = suop.find_all('a')
data = []
for a_tag in a_tags:
    url = 'https://vse-shutochki.ru' + a_tag['href']
    category = a_tag.text
    data.append([category, url])

print(data)