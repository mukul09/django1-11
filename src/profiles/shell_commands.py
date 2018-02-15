from django.contrib.auth import get_user_model

User=get_user_model()

r=User.objects.first()


#my followers
r.profile.followers.all()

#I am following
r.is_following.all()   # ==  r.profile.following.all()