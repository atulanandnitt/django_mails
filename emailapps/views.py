from django.shortcuts import render
from .models import *
from urllib import request
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .api import mailsserializer, inboxserializer, outboxserializer, draftserializer, replytoserializer
from rest_framework.response import Response
from send2trash import send2trash
from rest_framework.views import APIView
import time


class Inbox(APIView):

    def get(self, request):
        """

        :param request:
        :return:
        """
        global subject
        global attachment
        global message
        global from_email
        global qwes
        user = request.user
        qwes = User.objects.get(username=user).email
        mailbox = MailBox.objects.filter(recepient=qwes)
        print(mailbox)
        print("currently logged user ", qwes)
        print("mailbox", mailbox)

        print("inbox", Inbox)

        inn = Inboxs.objects.all().filter(recepient=qwes)
        serializer = inboxserializer(inn, many=True)
        hmtl = "in.html"
        return Response(serializer.data)


def home(request):
    temp = "email.html"
    return render(request, temp)


"""

def replyto(request):
    replyto = request.POST('replyto')
    #ui serializer code here
    if replyto:

        serializer = replytoserializer(#uiserializer)
        mol = Inboxs.objects.all().filter(message = serializer.data.message, sender = serializer.data.sender)


def forward(request):
    forward = request.post('forward')
    #ui serializer code here
    # can u pls write it ???
    if forward:
        #ui get objects here

"""

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('recepient', '')
    attachment = request.POST.get('attachment', '')
    print(attachment)
    user = request.user
    qwes = User.objects.get(username = user).email
    print(qwes)
    if subject and message:
        try:
            mail = MailBox(subject=subject, message=message, recepient=from_email, sender=qwes, attachment=attachment)
            inn = Inboxs(subject=subject, message=message, recepient=from_email, sender=qwes, attachment=attachment)
            mal = Outbox(subject=subject, message=message, recepient=from_email, sender=qwes)
            mal.save()
            inn.save()
            mail.save()

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('send_email')

        # In reality we'd use a form class
        # to get proper validation errors.
    return HttpResponse('mail sent')


class Maills(APIView):
    def get(self, request):
        mail = MailBox.objects.all()
        serializer = mailsserializer(mail, many=True)

        return Response(serializer.data)


class Outboxs(APIView):
    def get(self, request):
        user = request.user

        qwes = User.objects.get(username=user).email
        mailbox = Outbox.objects.all().filter(recepient=qwes)
        serializer = outboxserializer(mailbox, many=True)
        return Response(serializer.data)


def emailthread():
    mail = []
    if request.method == 'GET':#recepent, mail subject, mail body
        query = mail.objects.all()
        mail.push(query)
        ui = mail.pop()
        return JsonResponse({ui.data})


def trashcan(request):
    Trashbutton = request.POST.get("Delete")
    emaildetails = request.POST.get("message")

    #once Trashbutton is clicked on the UI
    if Trashbutton:
        Trashs = MailCompose.objects.all().filter(message=emaildetails)
        fork = Trash.save(Trash)
        Trashs.delete()#to delete from DB
        sent2trash(delete)#to delete from system,it cant be undone.


class Trash(APIView):
    """
    API return the mails in Trash folder.

    """
    def trashcan(request):
        user = request.user

        qwes = User.objects.get(username=user).email
        mailbox = Outbox.objects.all().filter(recepient=email)
        serialize = trashseralizer(mailbox, many=True)
        return Respose({serialize.data})


class Draftss(APIView):

    def get(self, request):
        draft_for_all_user = Drafts(subject=subject, message=message,
                                    recepient=from_email, sender=qwes, attachment=attachment)
        draft_for_all_user.save()
        draft_for_this_user = Drafts.objects.all().filter(email=send_email.qwes)
        serializer = draftserializer(draft_for_this_user, many=True)
        now = time.time()
        future = now + 10
        if now == future and send_mail.request.method is not "POST":
            return Response(serializer.data)
