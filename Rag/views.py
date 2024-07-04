from typing import Any
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article , Page , Question_and_Answer
from .forms import ArticleForm , QuestionForm
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

@login_required(login_url='login')
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
#  Profile.objects.get(user = request.user)
@login_required
def chatbot(request):
    # user_profile = request.user#.user_profile
    pages = Page.objects.filter(user_profile=request.user)
    print(pages[0].id) # f75eb1b0-0ce2-4a36-9d6f-179fc49263a9
    return render(request, 'chatbot.html', {'pages': pages , 'page':None })

# def page_detail(request, page_id): 
#     page = get_object_or_404(Page, id=page_id, user_profile=request.user.userprofile)
#     questions = page.questions.all()  # Use the related name 'questions' to fetch all related questions
#     return render(request, 'page_detail.html', {'page': page, 'questions': questions})

@login_required
def page_detail(request, id):

    page =  get_object_or_404(Page, id=id) #get_object_or_404(Page, id=id, user_profile=request.user.userprofile)
    # questions = page.questions.all()
    pages = Page.objects.filter(user_profile=page.user_profile) 
    print(request.user.email , page.user_profile.email)
    if request.user.email == page.user_profile.email:

        questions_and_answers = Question_and_Answer.objects.filter(page=page)
        # print(questions_and_answers[0].message)
        context = {
            'pages' : pages,
            'page': page, 
            'questions_and_answers': questions_and_answers,
        }
        
        if request.method == 'POST':
            print(request.POST)
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.page = page
                question.response = 'this is chat gpt'
                question.save()
                print('this is question',question)
                return redirect('chatbot_page' , id = page.id)
            else:  
                print('form is not valide') 
        else:
            
            form = QuestionForm()
            context['form'] = form 

        return render(request, 'chatbot.html', context)
    else:
        print('this is else')
        # redirect('home_page')
        raise Http404("Page not found")
 
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