from django.views import View
from django.conf import settings
from django.http import HttpResponse
import os
from xml.dom import minidom

class DemoXmlView(View):
    def get(self, request, *args, **kwargs):
        # get filename from url http://localhost:8000/demoxml/demo.xml
        # here demo.xml is file_name 
        file_name = kwargs['file_name']
        mediaurl = settings.MEDIA_ROOT
        file_path = f'{mediaurl}/xmlfiles/{file_name}'
        if os.path.exists(file_path):
            return HttpResponse(open(file_path).read(), content_type='text/xml')
        
        # redirect or return error if file not found
        return HttpResponse([])
        

    # uncomment below to add xsl stylesheet

    # def get(self, request, *args, **kwargs):
    #     file_name = kwargs['file_name']
    #     mediaurl = settings.MEDIA_ROOT

    #     file_path = f'{mediaurl}/xmlfiles/{file_name}'
    #     if not os.path.exists(file_path):
    #         # redirect or return error if file not found
    #         return HttpResponse([])

    #     dom = minidom.parse(f'{mediaurl}/xmlfiles/{file_name}')
    #     pi = dom.createProcessingInstruction('xml-stylesheet',
    #                                          'type="text/xsl" href="/static/xsl_styles/teibp.xsl"')
    #     root = dom.firstChild
    #     dom.insertBefore(pi, root)
    #     xml_data = dom.toxml()
    #     return HttpResponse(xml_data, content_type='text/xml')
