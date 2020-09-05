from django.urls import path
from .views import subscribe, general, sendmail, index, CreateImageView, doc, dir, searchposts, PositionIndexView, WorkersIndexView, DepartIndexView, PersonCreateForm, PersonEditView, PersonDeleteForm, PersonDetailView


urlpatterns = [
    path('', general, name= 'general'),
    path('sub/', subscribe, name= 'subscribe'),
    path('image/', CreateImageView.as_view(), name= 'image'),
    path('doc/', doc, name= 'doc'),
    path('sendmail/', sendmail, name= 'sendmail'),
    path('dir/', dir, name= 'dir'),
    path('index/', index, name= 'index'),
    path('position/', PositionIndexView.as_view(), name='position'),
    path('index/search/', searchposts, name='search'),
    path('workers/', WorkersIndexView.as_view(), name='workers'),
    path('depart/', DepartIndexView.as_view(), name='depart'),
    path('add/', PersonCreateForm.as_view(), name='add'),
    path('edit/<int:pk>/', PersonEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', PersonDeleteForm.as_view(), name='delete'),
    path('detail/<int:pk>/', PersonDetailView.as_view(), name='detail'),
]