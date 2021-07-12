from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from users.serializers import RegisterSerializer
from users.utils import Utils


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data["email"])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relative_link = reverse("email-verify")

        abs_url = "http://"+current_site + relative_link + "?token=" + str(token)
        email_body = f"Hi {user.user_name} \n  Please verify your email through the following link: {abs_url}"
        data = {"email_body": email_body, "email_subject": "Verify your email", "to_email": user.email}
        Utils.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)

class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        pass