import jwt
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

from django.conf import settings


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
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload["user_id"])

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({"email": "Successfully activated"}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as e:
            return Response({"error": "Activation link expired"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
