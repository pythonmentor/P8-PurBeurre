from django.shortcuts import render
from core.models import Product
from django.views.generic.list import ListView
#from django.views.generic import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

'''
def search(request):
    query = request.GET.get('query')
    print(query)
    result_list = Product.objects.filter(product_name__icontains=query)[:20]
    paginator = Paginator(result_list, 3)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    print(result_list)
    return render(request, 'search.html', {'results': results, 'query': query})
'''


class SearchView(ListView):
    model = Product
    context_object_name = 'results'
    paginate_by = 9
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('query')
        queryset = Product.objects.filter(product_name__icontains=query)
        page = self.request.GET.get('page')
        paginator = Paginator(queryset, self.paginate_by)

        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        context['results'] = results
        context['query'] = query
        return context


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
            product_nutriscore__lte=nutriscore, product_category__category_name=category
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

