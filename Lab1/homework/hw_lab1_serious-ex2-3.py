from pymongo import MongoClient

uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)

db = client.get_default_database()

posts = db['posts']

post = {
    'title': 'Suy nghĩ của Ngâng',
    'content': 'Học C4E vui mí lạ lạ. Nhiều lúc chết não nhưng vẫn thích. Techkids ai cũng đáng yêu.',
    'author': 'Hà Ngân'
}

posts.insert_one(post)
