from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Product, WishList
from .forms import ProductCreateForm


def index(request):
    wishlists = WishList.objects.filter(owner=request.user)
    context = {
        'title': 'Wishlist | Home page',
        'wishlists': wishlists,
    }
    return render(request, 'mainapp/index.html', context=context)


def contact(request):
    context = {
        'title': 'Wishlist | Contact Us'
    }
    return render(request, 'mainapp/contact.html', context=context)


def about(request):
    context = {
        'title': 'Wishlist | About project'
    }
    return render(request, 'mainapp/about.html', context=context)


def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk=pk)
    products = Product.objects.all()

    if request.method == 'POST' and 'title' in request.POST:
        product_form = ProductCreateForm(request.POST)
        if product_form.is_valid():
            product_form.save()
            wishlist_product_add = Product.objects.get(title=request.POST['title'])
            wishlist.products.add(wishlist_product_add)
            return HttpResponseRedirect(reverse('wish_list_page', args=[pk]))
    elif request.method == 'POST' and 'title' not in request.POST:
        product_form = ProductCreateForm()
        wishlist_product_add = Product.objects.get(pk=int(request.POST['select-exist']))
        wishlist.products.add(wishlist_product_add)
        return HttpResponseRedirect(reverse('wish_list_page', args=[pk]))
    else:
        product_form = ProductCreateForm()

    context = {
        'wishlist': wishlist,
        'wishlist_owner': wishlist.owner == request.user,
        'create_form': product_form,
        'products': products,
    }
    return render(request, 'mainapp/wish_list.html', context=context)
    