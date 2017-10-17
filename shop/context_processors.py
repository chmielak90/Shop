from .models import ProductCategory


def heddings_cp(request):
    heddings = ProductCategory.objects.filter(parent_category__isnull=True)

    categories = ProductCategory.objects.filter(parent_category__isnull=False)

    ctx = {
        'heddings': heddings,
        'categories': categories,
    }

    return ctx