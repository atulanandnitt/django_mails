from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import MailBox, Inboxs, Outbox, Trash, Drafts, ReplyTo


class Userss(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')
        #query = User.objects.get().values(fields)


class mailsserializer(serializers.ModelSerializer):
    class Meta:
        model = MailBox
        fields = ('sender', 'recepient', 'message', 'cc', "subject", "attachment")


class inboxserializer(serializers.ModelSerializer):
    class Meta:
        model = Inboxs
        fields = ('sender', 'message', 'cc', 'attachment', 'subject')


class outboxserializer(serializers.ModelSerializer):
    class Meta:
        model = Outbox
        fields = ('recepient', 'message', 'cc', 'attachment', 'subject')


class trashserializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ('recepient', 'message', 'cc', 'attachment', 'subject')


class draftserializer(serializers.ModelSerializer):
    class Meta:
        model = Drafts
        fields = ('recepient', 'message', 'cc', 'attachment', 'subject')


class replytoserializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyTo
        fields = ('recepient', 'message', 'subject')
