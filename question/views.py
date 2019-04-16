from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from question.fake_data import *

# Create your views here.

COUNT_POSTS_PER_PAGE = 5


def paginate(request, object_list):
    page = request.GET.get('page')
    p = Paginator(object_list, COUNT_POSTS_PER_PAGE)
    object_page = p.get_page(page)
    return object_page


def index(request):
    return render(request,
                  'index.html',
                  {
                      'page': paginate(request, questions),
                      'popular_tags': popular_tags,
                      'popular_members': popular_members
                  })


def question(request, question_id):
    return render_with_pagination(
        request,
        answers,
        {
            'question': questions[question_id],
            'popular_tags': popular_tags,
            'popular_members': popular_members
        },
        'question.html'
    )


def render_with_pagination(request, object_list, args_list, link='/'):
    return render(request,
                  link,
                  {
                      **{'page': paginate(request, object_list)},
                      **args_list
                  })


def tag(request, tag_name):
    questions_for_tag = create_questions_for_tag(tag_name)
    return render_with_pagination(
        request,
        questions_for_tag,
        {
            'tag_name': tag_name,
            'popular_tags': popular_tags,
            'popular_members': popular_members
        },
        'tag.html'
    )


def hot(request):
    return render_with_pagination(
        request,
        hot_questions,
        {
            'popular_tags': popular_tags,
            'popular_members': popular_members
        },
        'hot.html'
    )


def ask(request):
    return render(
        request,
        'ask.html',
        {
            'popular_tags': popular_tags,
            'popular_members': popular_members
        }
    )
