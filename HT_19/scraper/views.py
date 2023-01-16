from subprocess import call, run, PIPE

from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from scraper.models import Product, IdObject
# from scraper.subscraper import parse


def home(request):
    return render(request=request,
                  template_name='../templates/id_input_page.html')


def scraper(request: WSGIRequest):
    response = request.GET.get('id_string')
    if ';' in response:
        response.replace(';', '\n')
    if ',' in response:
        response.replace(',', '\n')
    if ' ' in response:
        response.replace(' ', '\n')
    if '\n\n' in response:
        response.replace('\n\n', '\n')
    response = response.split('\n')

    for id_obj in response:
        if id_obj != '':
            IdObject.objects.create(item_id=id_obj.strip())

    print('subprocess start')
    # call(['python', 'scraper/subscraper.py'])
    process = run(['python', 'scraper/subscraper.py'], stdout=PIPE)
    print('subprocess proceed')
    output = process.stdout

    return render(request=request,
                  template_name='../templates/my_products.html',
                  # context={'products': Product.objects.all()})
                  context={'products': output})


def my_products(request):
    return render(request=request,
                  template_name='../templates/my_products.html',
                  context={'products': Product.objects.all()})


def product_data(request, pk):
    pass
