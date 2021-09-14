from django.contrib import admin
from .models import News
from django.urls import reverse, NoReverseMatch
from django.utils.html import format_html


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'source')
    # readonly_fields = ('show_link',)
    #
    # def show_link(self, instance):
    #     url = reverse('newsfeed:home', kwargs={'pk': instance.pk})
    #     return format_html("""<a href="{0}">{0}</a>""", url)
    #
    # show_link.short_description = "News URL"
