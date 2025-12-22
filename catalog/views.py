from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    """Контроллер главной страницы с товарами"""
    products = Product.objects.all()
    context = {"products": products, "title": "Главная страница"}

    return render(request, "catalog/home.html", context)

def contacts(request):
    """Контроллер страницы с контактами"""

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        context = {
            "message_sent": True,
            "name": name,
            "email": email,
            "message": message,
        }
        return render(request, "catalog/contacts.html", context)
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    """Контроллер для отображения детальной информации о товаре"""
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product, "title": product.name}

    return render(request, "catalog/product_detail.html", context)
