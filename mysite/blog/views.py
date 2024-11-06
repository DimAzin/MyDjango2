from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    # Получаем количество постов на странице из GET-запроса (по умолчанию 5)
    posts_per_page = request.GET.get('posts_per_page', 5)

    # Преобразуем в целое число
    posts_per_page = int(posts_per_page)

    # Создаем пагинатор
    paginator = Paginator(posts, posts_per_page)

    # Получаем текущую страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'posts_per_page': posts_per_page,
    }

    return render(request, 'blog/post_list.html', context)
