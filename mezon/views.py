from django.shortcuts import get_object_or_404, render

from .models import Product, Category

def home(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    
    return render(request, 'home.html', context={'products':products, 'categories':categories})

def about_us(request):

    return render(request,'about_us.html',)

def product_list(reuqest):
    products = Product.objects.all()

    q = reuqest.GET.get('q')

    if q:
        products = Product.objects.filter(title__icontains=q)
    
    return render(reuqest, 'product_list.html', context={'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'product_detail.html', context={'product':product})

def category_products(request, pk):

    category = get_object_or_404(
        Category,
        pk=pk
    )

    products = category.products.all()

    q = request.GET.get('q')

    if q:
        products = Product.objects.filter(title__icontains=q)

    return render(
        request,
        'category_products.html',
        {
            'category': category,
            'products': products,
        }
    )

