from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index.html')

name = "color"
my_list = ["синий", "красный", " зеленый", "желтый"]
value = [1, 2]

books = [
    {"title": "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title": "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title": "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title": "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title": "Игрок",
     "author": "Достоевский Ф.М.",
     "price":  234.55}
]

html = template.render(content=books,
                       start=3,
                       end=7,
                       length=len
                       )

f = open('test1.html', 'w', encoding='utf-8-sig')
f.write(html)
f.close()
