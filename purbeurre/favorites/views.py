from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse, redirect
from favorites.models import Favorite
from core.models import Product
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views.generic.edit import ProcessFormView
#from forms import SaveForm

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
            )
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
