from django.urls import path, include
from .views import DemoXmlView

urlpatterns = [
    # file_name ==> File Name with extension ==> eg: demo_xml_file.xml
    path('demoxml/<file_name>', DemoXmlView.as_view(),
         name='demoxml'),
]
