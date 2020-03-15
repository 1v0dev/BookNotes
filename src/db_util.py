import hashlib

from pymongo import MongoClient
import config as cfg


client = MongoClient(host=cfg.mongo_host, port=cfg.mongo_port, username=cfg.mongo_username, password=cfg.mongo_password)
notes_db = client.book_notes


random_sample = [
    {"$lookup": {
        "from": "category",
        "localField": "category_id",
        "foreignField": "_id",
        "as": "category"
    }},
    {"$unwind": "$category"},
    {"$match": {"category.show_random": True}},
    {"$sample": {"size": 1}}
]


def find_random_note():
    random_note_list = list(notes_db.notes.aggregate(random_sample))
    if random_note_list:
        return dict(note=random_note_list[0])
    else:
        return dict(note=dict(category=dict(title='No notes'),
                              text='', location=''))


def new_category(title, title_hash=None):
    if not title_hash:
        title_hash = hashlib.md5(title.encode('utf-8')).hexdigest()
    category = {
        'title': title,
        'title_hash': title_hash,
        'show_random': True
    }
    return notes_db.category.insert_one(category)
