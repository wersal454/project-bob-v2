"""boreber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from boreber.quiz import views
from django.contrib import admin
from boreber.quiz.views import *
from django.urls import path, include
from accounts.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Category', CategoryViewSet)
router.register(r'Question', QuestionViewSet)
router.register(r'Choice', ChoiceViewSet)
router.register(r'Answer', AnswerViewSet)

urlpatterns = [
    path('', views.index)
]
router_ = [
    path('project/', include(router.urls))
]

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_)),
    path('login/', AuthorizationUserView.as_view(), name='login'),
    path('registr/', RegistrationUserView.as_view(), name='registr'),
]