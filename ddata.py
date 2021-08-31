from django.contrib.auth.models import User
from blog.models import Post
user = User.objects.get(username='Modric')
post= Post(title='WCKD is good',
        slug='wckd-is-good',
        body='Remember! WCKD is good',
        author=user,
        status='published')
post.save()


post1= Post(title='Hope is a dangerous thing',
        slug='hope-is-a-dangerous-thing',
        body='Hope is a dangerous things. It has killed more of my friends than the flare and the scorch combined',
        author=user,
        status='published')
post1.save()

 
post2= Post(title='Questions',
        slug='questions',
        body="I've got 3 questions for you- Where you goin? Where you from ? and how can I profit?",
        author=user,
        status='published')
post2.save()

 
post3= Post(title="Alby didn't die for nothing",
        slug="alby-didnt-die-for-nothing",
        body="If we quit trying then Alby did for nothing and I can't have that.",
        author=user,
        status='published')
post3.save()
