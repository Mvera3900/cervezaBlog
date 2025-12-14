from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

#return HttpResponse ("Bienvenido a la página principal").
def index (request):
    #posts_destacados = Post.objects.filter(destacado=True)
    #ultimospost = Post.objects.all().order_by('fecha_publicacion').reverse[:3]
    return render (request, 'index.html') #(ultimospost))

def about_view (request):
    return render (request, 'about.html')

def contact_view (request):
    return render (request, 'contact.html')

# para ver el articulo completo 
def post_detail(request, pk):
    # Busca el Post con ese ID, si no lo encuentra, lanza el error 404
    post = get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.filter(comentario_padre=None).order_by('-fecha_creacion')

#    if request.method == 'POST':
#       if request.user.is_authenticated:
#            form= ComentarioForm(request.POST)
#            if form.is_valid():
#                comentario = form.save(commit=False)
#                comentario.post = post
#                comentario.usuario = request.user
#                comentario.save()
#                return redirect('post_detail', pk=post.pk)
#            else:
#                return redirect('post_detail', pk=post.pk)
#        else:
#            return redirect('login')
#    else:
#        form = ComentarioForm()
        
#    return render(request, 'blogInfo/post_detail.html', {
#        'post': post,
#        'comentarios': comentarios,
#        'form': form
#        })

#def responder_comentario(request, pk):
#    # busca el comentario que se comenta
#    comentario_padre = get_object_or_404(Comentario, pk=pk)

#    if request.method == 'POST':
#        form = ComentarioForm(request.POST)
#        if form.is_valid():
#            respuesta = form.save(commit=False)
#            respuesta.usuario = request.user
#            respuesta.post = comentario_padre.post
#            respuesta.comentario_padre = comentario_padre
#            respuesta.save()
#            return redirect('post_detail', pk=comentario_padre.post.pk)
#    else:
#        form = ComentarioForm() 
#    return render(request, 'blogInfo/responder.html',{
#        'form': form,
#        'comentario_padre': comentario_padre
#    })
