from django.conf.urls import url
from shop import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^men$', views.Man.as_view()),
    url(r'^women$', views.Woman.as_view()),
    url(r'^mail$', views.Mail.as_view()),
    url(r'^product$', views.SingleProduct.as_view()),
    url(r'^checkout$', views.Checkout.as_view()),
]
