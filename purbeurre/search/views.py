from core.models import Product
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


class SearchView(ListView):
    model = Product
    context_object_name = "results"
    paginate_by = 9
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get("query")
        queryset = Product.objects.filter(product_name__icontains=query).order_by('product_name')
        page = self.request.GET.get("page")
        paginator = Paginator(queryset, self.paginate_by)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)

        context["results"] = results
        context["query"] = query
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
    slug_field = "product_code"
    slug_url_kwarg = "code"
