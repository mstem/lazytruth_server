from apps.data.models import *
from django.contrib import admin


class RumorInlineAdmin(admin.TabularInline):
    model = Rumor
    extra = 0
    #classes = ('collapse open',)



class RumorAdmin(admin.ModelAdmin):
    #list_filter    = ('refuted',)
    search_fields = ['text','fact']
    list_display = ('id','title','text','fact')
    #exclude = ('keys',)


class FactAdmin(admin.ModelAdmin):
    list_filter    = ('source',)
    search_fields = ('source','text')
    list_display = ('id','title','source','text')
    inlines = [RumorInlineAdmin]

class SourceAdmin(admin.ModelAdmin):
    search_fields = ['url','name']
    list_display = ('id','url','name',)

admin.site.register(Fact,FactAdmin)
admin.site.register(Rumor,RumorAdmin )
admin.site.register(Source,SourceAdmin)