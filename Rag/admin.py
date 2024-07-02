from django.contrib import admin
from .models import Article ,Page , Question_and_Answer
# Register your models here.

admin.site.register(Article)
admin.site.register(Page)
admin.site.register(Question_and_Answer)