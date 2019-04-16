import random
from faker import Faker

fake = Faker()

questions = []
for i in range(0, 70):
    questions.append({
        'id': i,
        'title': fake.sentence(),
        'content': fake.text(),
        'tag': 'tag' + str(i),
        'rating': random.randint(0, 5000),
        'answers': random.randint(0, 100)
    })

hot_questions = []
for i in range(10):
    hot_questions.append({
        'title': fake.sentence(),
        'id': i,
        'content': fake.text(),
        'tag': 'tag' + str(i),
        'rating': i * (15 + i),
        'answers': random.randint(0, 100)
    })
hot_questions.reverse()

answers = []
for i in range(0, 20):
    answers.append({
        'rating': random.randint(0, 1000),
        'id': i,
        'content': fake.text()
    })

popular_tags = []
for i in range(10):
    popular_tags.append({
        'tag_name': "tag" + str(i)
    })

popular_members = []
for i in range(7):
    popular_members.append({
        'member_name': fake.name()
    })


def create_questions_for_tag(tag_name):
    questions_for_tag = []
    for i in range(0, 15):
        questions_for_tag.append({
            'title': fake.sentence(),
            'id': i,
            'content': fake.text(),
            'tag': tag_name,
            'rating': random.randint(0, 5000),
            'answers': random.randint(0, 100)
        })
    return questions_for_tag
