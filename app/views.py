from django.shortcuts import render
import datetime
from django.views.generic.list import ListView
from .models import User, Posts
from .forms import PostForm

# Create your views here.
def index(request):
    # date = datetime.datetime.now().strftime('%H:%M:%S')  
    return render(request,'index.html')

class AddPostView(ListView):
    model = Posts

    def get(self, request):
        form = PostForm()
        return render(request, 'editor.html', {'form':form})
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            # userName = form.cleaned_data['userName']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # user_obj = User.objects.get(username=userName)
            add_post = Post.objects.create(title=title, content=content)
            add_post.save()
            form = PostForm()
            return render(request,'editor.html',{'form':form})


class SeePostView(AddPostView):
    model = Posts

    def get(self,request):
        all_post = self.model.objects.all().order_by('-id')
        return render(request, 'slider.html', {'posts':all_post})
