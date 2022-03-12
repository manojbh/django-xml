# XML Django

Xml file is in media/xmlfiles folder
xsl file with js and css is in static/xsl_styles folder
views are on home app

## Add on settings.py

```sh
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
MEDIA_URL = '/media/'
```

## Add below url on xmldemo/urls.py
```sh
url(r'^(?!/?static/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),
```
## Run


```sh
python manage.py runserver
```

## Files to look into
- xmldemo/urls.py
- xmldemo/settings.py
- home/urls.py
- home/views.py
- static/
- media/