from django.urls import path
from . import views

urlpatterns = [
    path("baraa/", views.show_baraa_form, name="show_baraa"),
    path("cart/", views.show_cart, name="cart"),
    path("dashboard/", views.show_dashboard, name="dashboard"),
    path("order-complete/", views.show_order_complete, name="order-complete"),
    path("place-order/", views.show_place_order, name="place-order"),
    path("product-detail/", views.show_product_detail, name="product-detail"),
    path("register/", views.show_register, name="register"),
    path("search-result/", views.show_search, name="search-result"),
    path("signin/", views.show_signin, name="signin"),
    path("store/", views.show_store, name="store"),
    path("", views.index, name="index"),

]

