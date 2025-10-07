from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from store_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('store/', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('register/', views.register, name='register'),
    path('signin/', views.signin, name='signin'),
    path('search/', views.search_result, name='search_result'),
    path('order-complete/', views.order_complete, name='order_complete'),

    # Хэрэв store_app-д өөр urls.py байгаа бол
    # path('store/', include('store_app.urls')),
]

# Media файлуудыг serve хийх (DEBUG=True үед)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
