from django.conf.urls import url

from . import views

app_name='doctors'

urlpatterns=[
			url(r'^$',views.login,name='login_page'),
			url(r'^prescription/$',views.prescription,name='prescription_page'),
			#url(r'^doctors/(\d+)$',views.accountPage,name='account_page')
			 ]

