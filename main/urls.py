from django.urls import path
from main.views import show_main, create_product, show_html, show_xml, show_json, show_xml_by_id, show_json_by_id, delete_product, increase_product_quantity, decrease_product_quantity


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('increase_product_quantity/<int:id>/', increase_product_quantity, name='increase_product_quantity'),
    path('decrease_product_quantity/<int:id>/', decrease_product_quantity, name='decrease_product_quantity'),
]