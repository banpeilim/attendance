from django.urls import path
from . import views


urlpatterns = [
    path('flight-data/', views.getFlights, name="routes"),
    path('update-review/', views.updateReview, name="update_review"),
    path('data-page/', views.dataPage.as_view(), name="data_page"),
    path('update-attendance/', views.updateAttendance, name="update_attendance"),
    path('attendance-page/', views.attendancePage, name="attendace_page"),
    path('add-queue/', views.addQueue, name="add_queue"),
    path('queue-data/', views.getQueue, name="queue"),
    path('inventory-data/', views.getInventory, name="inventory_data"),

]