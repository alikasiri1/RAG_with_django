from typing import Any
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article , Page
from .forms import ArticleForm , QuestionForm
from django.contrib.auth.decorators import login_required
from users.models import Profile

def homepage(request):
    return render(request , 'home.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, id):
    article = get_object_or_404(Article, id=id)  #  == Article.objects.get(id = id)
    print(article.content , article.id)
    print(request.path_info , print(type(request)))
    return render(request, 'article_detail.html', {'article': article})

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})

def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'article_form.html', {'form': form})

def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'article_confirm_delete.html', {'article': article})




#######################################
@login_required
def dashboard(request):
    user_profile = request.user.user_profile
    pages = user_profile.pages.all()
    return render(request, 'dashboard.html', {'pages': pages })

# def page_detail(request, page_id):
#     page = get_object_or_404(Page, id=page_id, user_profile=request.user.userprofile)
#     questions = page.questions.all()  # Use the related name 'questions' to fetch all related questions
#     return render(request, 'page_detail.html', {'page': page, 'questions': questions})

@login_required
def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id, user_profile=request.user.userprofile)
    questions = page.questions.all()
    
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.page = page
            question.save()
            return redirect('page_detail', page_id=page.id)
    else:
        form = QuestionForm()

    return render(request, 'page_detail.html', {
        'page': page,
        'questions': questions,
        'form': form
    })

# @login_required
# def create_question(request, page_id):
#     page = get_object_or_404(Page, id=page_id, user_profile=request.user.userprofile)
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.page = page
#             question.save()
#             return redirect('page_detail', page_id=page.id)
#     else:
#         form = QuestionForm()
#     return render(request, 'create_question.html', {'form': form, 'page': page})