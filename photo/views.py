from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo 

class PhotoList(ListView):
    model = Photo
    templates_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo 
    fields = ['author','text', 'image']
    templates_name_suffix = '_create'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})


class PhotoUpdate(UpdateView):
    model = Photo 
    fields = ['author','text', 'image']
    templates_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    model = Photo 
    templates_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DetailView):
    model = Photo 
    templates_name_suffix = '_datail'
  
