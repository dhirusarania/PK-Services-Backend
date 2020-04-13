from rest_framework import generics
from rest_framework.views import APIView
from .serializer import createQuerySerializer, createContactSerializer
from Queries.models import CareerQuery, ContactUs
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status
from django.utils.html import strip_tags
import json
from django.core.mail import EmailMessage

class createQuery(generics.CreateAPIView):

    serializer_class        = createQuerySerializer
    queryset                = CareerQuery.objects.all()

class createContact(generics.CreateAPIView):

    serializer_class        = createContactSerializer
    queryset                = ContactUs.objects.all()


class sendMail(APIView):

  def post(self, request, format=None):
      

        print("email)")
        email = json.loads(request.body)['email']


        print(email)
        msg_html = render_to_string('../templates/email.html')
        owner_msg_html = render_to_string('../templates/email_owner.html', {'email': email})

        send_mail(
            'Thank you for getting in touch!',
            strip_tags(msg_html),
            'pawan@pkservices.in',
            [email, 'tecmeadows.office@gmail.com'],
            fail_silently=False,
            html_message=msg_html
        )

        # print(email)


        # email = EmailMessage(
        #     'subject',
        #     'message.',
        #     'pawan@pkservices.in',
        #     to=[email],
        #     headers={'mailed-by':  'pkservices.in', 'signed-by':  'pkservices.in'},
        # )

        # email.send(fail_silently=False)

        send_mail(
            'You have a new Query.',
            strip_tags(msg_html),
            'pawan@pkservices.in',
            ['pawan@pkservices.in', 'dhirusarania@gmail.com'],
            fail_silently=False,
            html_message=owner_msg_html
        )

        print(status)


        # ContactUs.objects.create(email = email, subject = 'Footer Query')

        return Response({}, status=status.HTTP_200_OK)
