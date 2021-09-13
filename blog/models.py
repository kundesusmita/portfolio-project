from django.db import models

# Create a blog models
# title
# pub_date
# body
# image


# Add blog app to settings
# create a migration
# migrate
# add to admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    
