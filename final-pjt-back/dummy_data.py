from django.contrib.auth import get_user_model
from django.utils import timezone
from random import randint, sample
from faker import Faker
from random import choice
from articles.models import Article, Comment

'''
accounts와 articles 더미데이터 생산 스크립트 파일입니다.
python manage.py shell에 접속하여 이 코드를 그대로 실행해주세요.
exit()하면 shell에서 탈출합니다.
'''

fake = Faker()
User = get_user_model()
users = User.objects.all()

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# Create dummy users
for _ in range(30):
    username = fake.user_name()
    email = fake.email()
    password = fake.password()
    mbti = choice(mbti_types)  # Randomly select one MBTI type
    User.objects.create_user(username=username, email=email, password=password, mbti=mbti)


# Create dummy articles
for _ in range(60):
    user = users[randint(0, 29)]  # Select a random user
    title = fake.sentence(nb_words=5)
    content = fake.paragraph()
    image = 'example.jpg'
    created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
    Article.objects.create(user=user, title=title, content=content, image=image, created_at=created_at)


articles = Article.objects.all()

# Create dummy comments
for _ in range(150):
    article = articles[randint(0, 59)]  # Select a random article
    user = users[randint(0, 29)]  # Select a random user
    content = fake.paragraph()
    created_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone())
    Comment.objects.create(article=article, user=user, content=content, created_at=created_at)

# Create dummy like_users
for article in articles:
    like_users_count = randint(0, 15)  # Randomly determine the number of like_users
    like_users = sample(list(users.exclude(pk=article.user.pk)), like_users_count)
    
    for user in like_users:
        article.like_users.add(user)

# Create dummy followings and followers
for user in users:
    followings_count = randint(0, 15)  # Randomly determine the number of followings
    followings = sample(list(users.exclude(pk=user.pk)), followings_count)
    
    for followed_user in followings:
        user.followings.add(followed_user)
        followed_user.followers.add(user)
