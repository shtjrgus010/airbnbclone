from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    search_fields = (
        "name",
        "^price",
        "owner__username",
    )

    list_filter = (
        "price",
        "rooms",
        "toilets",
        "description",
        "address",
        "pet_friendly",
        "kind",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )
