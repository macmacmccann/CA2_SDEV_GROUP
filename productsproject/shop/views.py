from django.views.generic import TemplateView, ListView
from django.shortcuts import render , get_object_or_404
from shop.models import Category,Product 
from django.core.paginator import Paginator,EmptyPage,InvalidPage


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'



def cat_list(request):
    categories= Category.objects.all()
    return render(request, 'shop/category.html', {'cats': categories})
    

def products_by_category(request, category_id):
    category= get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/products_by_category.html', {'category': category, 'products': products})


def prod_list(request,category_id= None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)

    paginator = Paginator (products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)


    return render( request, 'shop/category.html', {'cats':category, 'prods':products})

def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'shop/product.html', {'product':product})


class SearchResultsListView(ListView):
    model = Product 
    context_object_name = 'product_list'
    template_name = 'products/search_results.html'
    # If i wanted to only show what has "django" in the name value
    #queryset = Product.objects.filter(name__icontains='Django')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains='query') | Q(category__icontains='query'))
