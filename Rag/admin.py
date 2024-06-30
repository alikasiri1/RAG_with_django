from django.contrib import admin
from .models import Article ,Page , Question , Answer
# Register your models here.

admin.site.register(Article)
admin.site.register(Page)
admin.site.register(Question)
admin.site.register(Answer)