from django.shortcuts import render
from django.shortcuts import HttpResponse
from favorites.models import Favorites
from core.models import Product
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views.generic.edit import ProcessFormView
#from forms import SaveForm

# Create your views here.


class SaveFavoritesView(View):

    def post(self, request, *args, **kwargs):
        code = self.request.POST.get('code')
        code = Product.objects.get(pk=code)
        user = self.request.user.id

        print(code, user)
        Favorites(favorite_code=code, user_id=user).save()
        return render(request, template_name='base.html')


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
        return context_data
