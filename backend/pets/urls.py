from django.urls import path
from pets.views import PetListView, PetCreateView, PetRetrieveView, PetUpdateView, PetDestroyView

app_name = "pets"

urlpatterns = [
    path("list/", PetListView.as_view(), name="pet_list"),
    path("create/", PetCreateView.as_view(), name="pet_create"),
    path("<int:pk>/", PetRetrieveView.as_view(), name="pet_get"),
    path("<int:pk>/update", PetUpdateView.as_view(), name="pet_update"),
    path("<int:pk>/delete", PetDestroyView.as_view(), name="pet_delete"),
]