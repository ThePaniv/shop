from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.renderers import TemplateHTMLRenderer
from shop.forms import EmailForm
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView

from shop.models import Product
from django.contrib.sessions.models import Session


class Index(LoginRequiredMixin, APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        first_4_products = products[:4]
        last_4_products = products[::-1][:4]
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return Response(data={'products': products, 'first_4_products': first_4_products, 'last_4_products': last_4_products, 'username': user.username})


class Man(LoginRequiredMixin, APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'man.html'

    def get(self, request, *args, **kwargs):
        man_products = Product.objects.filter(category_id=1)
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return Response(data={'products': man_products, 'username': user.username})


class Checkout(LoginRequiredMixin, APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'checkout.html'

    def get(self, request, *args, **kwargs):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return Response(data={'username': user.username})


class Woman(LoginRequiredMixin, APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'woman.html'

    def get(self, request, *args, **kwargs):
        woman_products = Product.objects.filter(category_id=2)
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return Response(data={'products': woman_products, 'username': user.username})


class Mail(APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'mail.html'

    def get(self, request, *args, **kwargs):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        return Response({'username': user.username})

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        form.is_valid()
        data = form.cleaned_data
        send_mail(
            'Customer contact',
            f'Message from {data["name"]} with email {data["email"]}:\n{data["message"]}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return Response()


class SingleProduct(LoginRequiredMixin, APIView):
    login_url = 'accounts/login/'
    renderer_classes = [TemplateHTMLRenderer]
    queryset = User.objects.all()
    template_name = 'single.html'

    def get(self, request, *args, **kwargs):
        session = Session.objects.get(session_key=request.session.session_key)
        session_data = session.get_decoded()
        uid = session_data.get('_auth_user_id')
        user = User.objects.get(id=uid)
        product_id = request.GET.get('id')
        product = Product.objects.filter(id=product_id).first()
        return Response({'username': user.username, 'product': product})


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(template_name='login.html')


