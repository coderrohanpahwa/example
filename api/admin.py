from django.contrib import admin
from .models import MyModel
from django.urls import reverse
from django.utils import html
from django.urls import reverse
from django.template.response import TemplateResponse
# Register your models here.
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
def make_completed(modeladmin, request, queryset):
    queryset.update(choice='1')
def make_uncomplete(modeladmin,request,queryset):
    queryset.update(choice='2')
@admin.register(MyModel) #  <====
class cust(admin.ModelAdmin):
    print("Chal rha hai ")
    list_display = ['title','link','choice']
    actions = [make_completed,make_uncomplete]
    def link(self,obj):
        # =>/admin/app_name/id
        url=f'{obj.id}'
        # url=reverse('admin/app/'+str(obj.id))
        return html.format_html('<a href="{url}">Click Me</a>', url=url)

    def get_urls(self):
            urls = super().get_urls()
            my_urls = [
                path('my_view/', self.my_view),
            ]
            print(urls)
            print(my_urls)
            return my_urls + urls
    @method_decorator(login_required)
    def my_view(self, request):
            context = dict(
                # Include common variables for rendering the admin template.
                self.admin_site.each_context(request),
                # Anything else you want in the context...
               name="rohan",
            )
            print(context)
            return TemplateResponse(request, "api/about.html", context)

