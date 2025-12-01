from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """Serialize Listing model for API responses."""
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'price_per_night',
            'max_guests', 'address', 'city', 'country',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    """Serialize Booking model."""
    listing_title = serializers.CharField(source='listing.title', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest_name',
            'guest_email', 'check_in', 'check_out',
            'number_of_guests', 'total_price', 'created_at'
        ]
        read_only_fields = ['total_price', 'created_at']