from .models import Category
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


#in any templates we can use menu_linls so we create context file    
#This is a context processor used to send categories to all templates.