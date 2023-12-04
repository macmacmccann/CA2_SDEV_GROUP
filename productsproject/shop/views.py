from django.views.generic import TemplateView, ListView
from django.shortcuts import render , get_object_or_404
from shop.models import Category,Product 
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.views.generic.edit import CreateView
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'



class CreateProductView(CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image', 'stock', 'available')
    template_name = 'shop/new_product.html'

    def get_success_url(self):
            return reverse('success_url_name')  # Replace 'success_url_name' with the name of your success URL



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
    context_object_name = 'prod_list'
    template_name = 'products/search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter( Q(name__icontains=query) | Q(category__name__icontains=query))
           # Product.objects.filter(name__icontains='Python')

