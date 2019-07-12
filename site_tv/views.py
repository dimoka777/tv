from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.db.models.functions import Length
from .models import Post, Choice


class SubPostListView(ListView):
    model = Post
    template_name = 'post_list.html'


class SubAgent(CreateView):
    model = Post
    template_name = 'main.html'
    fields = [ 'price', 'text', 'post_dates']
    success_url = '/'

    def post(self, request, *args, **kwargs):
        self.object = None
        if request.method == "POST":
            # for item in self.object:
            #     print(item.price.price)
            obj = Post.objects.get(pk=request.POST['id'])
            print(obj)
            text = request.POST['text']
            print(len(text))
            post_dates = request.POST['post_dates']
            Post.objects.create(
                text=text,
                post_dates=post_dates,
            )
        else:
            print("nnn")
        return super().post(request, *args, **kwargs)


