from . models import Category

def nemu_links(request):
    
    links = Category.objects.all()
    
    return dict(links=links)