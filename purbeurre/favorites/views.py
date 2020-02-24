from core.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect, render
from django.urls import reverse
from django.views.generic.base import View
from django.views.generic.list import ListView
from favorites.models import Favorite

# Create your views here.


class SubstituteView(ListView):

    model = Product
    template_name = 'substitutes.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context_data = super(SubstituteView, self).get_context_data(**kwargs)
        code = self.request.GET.get('code')
        category = self.request.GET.get('category')
        nutriscore = self.request.GET.get('nutriscore')
        page = self.request.GET.get('page')
        queryset = Product.objects.filter(
            product_nutriscore__lte=nutriscore,
            product_category__category_name=category
            ).order_by('product_nutriscore')
        paginator = Paginator(queryset, self.paginate_by)

        try:
            subs = paginator.page(page)
        except PageNotAnInteger:
            subs = paginator.page(1)
        except EmptyPage:
            subs = paginator.page(paginator.num_pages)

        context_data['to_sub'] = Product.objects.get(product_code=code)
        context_data['subs'] = subs

        for sub in subs:
            if self.request.user.id:
                sub.saved = Favorite.is_favorite(sub, self.request.user)
            else:
                sub.saved = False

        return context_data

    def post(self, request, *args, **kwargs):
        code = self.request.POST.get('code')
        product = Product.objects.get(pk=code)
        user = self.request.user
        Favorite(product=product, user=user).save()
        return redirect(request.get_full_path())


class FavoritesView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Favorite
    template_name = 'favorites.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context_data = super(FavoritesView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        user = self.request.user
        queryset = Favorite.objects.filter(user=user)
        paginator = Paginator(queryset, self.paginate_by)

        try:
            favs = paginator.page(page)
        except PageNotAnInteger:
            favs = paginator.page(1)
        except EmptyPage:
            favs = paginator.page(paginator.num_pages)

        context_data['favs'] = favs

        return context_data
