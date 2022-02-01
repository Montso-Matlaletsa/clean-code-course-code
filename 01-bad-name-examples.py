from datetime import datetime


class BlogPost:
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date


def printPost(item):
    print('Title: ' + item.title)
    print('Description: ' + item.description)
    print('Published: ' + item.date)


summary = 'Clean Code Is Great!'
description = 'Actually, writing Clean Code can be pretty fun. You\'ll see!'
new_date = datetime.now()
publish = new_date.strftime('%Y-%m-%d %H:%M')

post = BlogPost(summary, desc, publish)

printPost(post)
