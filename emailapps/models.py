from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
 
LIMIT_FOR_MAIL = 1000000000
LIMIT_FOR_CC = 10000
LIMIT_FOR_TO = 10000
LIMIT_FOR_ATTACHMENTS = 100


class MailBox(models.Model):

    global LIMIT_FOR_MAIL
    global LIMIT
    message = models.TextField(default="", max_length=LIMIT_FOR_MAIL)
    # editable=False, beacuse once a user logged in it shouldnt get updated.
    sender = models.EmailField(default=User, editable=False)
    recepient = models.CharField(default="", max_length=100)
    subject = models.CharField(default="", max_length=LIMIT_FOR_CC)
    attachment = models.FileField(default="")
    a = []
    lenght = len(a)
    cc = models.CharField(default=a,max_length=LIMIT_FOR_CC)
    objects = models.Manager()

    def __str__(self):
            return self.message[:50] + '...'


class Inboxs(MailBox):
      mail = MailBox
               
       
class Drafts(MailBox):
     
    mail = MailBox
   

# auto complete of the email address from DB :
# what we can do is  choices=("at":"atul.anand.nitt@gmail.com")


class Outbox(MailBox):
    mail = MailBox


class ReplyTo(MPTTModel):
    message = models.ForeignKey(MailBox, related_name='comments', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)
    reply = models.CharField(max_length=500, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
            order_insertion_by = ['date_added']

            def __str__(self):
                return self.user_reply[:20]


class Trash(MailBox):

    mail = MailBox






    