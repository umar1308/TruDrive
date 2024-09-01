from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('index/',views.index,name='index'),
    path('booking/',views.booking,name='booking'),
    path('operatorlist/',views.operatorlist,name='opeartorlist'),
    path('people/<int:id>/', views.person_detail, name='person_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
