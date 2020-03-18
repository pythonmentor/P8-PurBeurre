from core.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.views.defaults import bad_request
from django.views.generic.list import ListView
from favorites.models import Favorite

# Create your views here.


class SubstituteView(ListView):

    model = Product
    template_name = "substitutes.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context_data = {}
        if isinstance(self.request.GET.get("code"), str):
            code = self.request.GET.get("code")
        else:
            return context_data

        if isinstance(self.request.GET.get("category"), str):
            category = self.request.GET.get("category")
        else:
            return context_data

        if self.request.GET.get("nutriscore") in ["a", "b", "c", "d", "e"]:
            nutriscore = self.request.GET.get("nutriscore")
        else:
            return context_data

        context_data = super(SubstituteView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        queryset = get_list_or_404(
            Product.objects.filter(
                product_nutriscore__lte=nutriscore,
                product_category__category_name=category,
            ).order_by("product_nutriscore")
        )
        paginator = Paginator(queryset, self.paginate_by)

        try:
            subs = paginator.page(page)
        except PageNotAnInteger:
            subs = paginator.page(1)
        except EmptyPage:
            subs = paginator.page(paginator.num_pages)

        context_data["to_sub"] = Product.objects.get(product_code=code)
        context_data["subs"] = subs

        for sub in subs:
            if self.request.user.id:
                sub.saved = Favorite.is_favorite(sub, self.request.user)
            else:
                sub.saved = False

        return context_data

    def post(self, request, *args, **kwargs):
        try:
            int(self.request.POST.get("code"))
            code = self.request.POST.get("code")
            if Favorite.objects.filter(product__product_code=code).exists():
                raise ValueError
            else:
                product = get_object_or_404(Product, pk=code)
                user = self.request.user
                Favorite(product=product, user=user).save()
        except ValueError:
            return bad_request(self.request, ValueError, template_name="400.html")
        return redirect(request.get_full_path())


class FavoritesView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    model = Favorite
    template_name = "favorites.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context_data = super(FavoritesView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page")
        user = self.request.user
        queryset = Favorite.objects.filter(user=user)
        paginator = Paginator(queryset, self.paginate_by)

        try:
            favs = paginator.page(page)
        except PageNotAnInteger:
            favs = paginator.page(1)
        except EmptyPage:
            favs = paginator.page(paginator.num_pages)

        context_data["favs"] = favs

        return context_data
