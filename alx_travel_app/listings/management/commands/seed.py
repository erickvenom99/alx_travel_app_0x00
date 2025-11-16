import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import Listing, Booking, Review


CITIES = [
    ("Paris", "France"),
    ("Tokyo", "Japan"),
    ("New York", "USA"),
    ("Barcelona", "Spain"),
    ("Cape Town", "South Africa"),
]

TITLES = [
    "Cozy Studio in City Center",
    "Luxury Villa with Ocean View",
    "Modern Loft near Metro",
    "Rustic Cabin in the Woods",
    "Penthouse with Skyline View",
]

DESCRIPTIONS = [
    "A charming apartment with all amenities.",
    "Spacious house perfect for families.",
    "Stylish loft with exposed brick walls.",
    "Peaceful retreat surrounded by nature.",
    "Elegant penthouse with panoramic views.",
]


class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings and reviews."

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # ---- Create 10 Listings ----
        listings = []
        for i in range(10):
            city, country = random.choice(CITIES)
            listing = Listing(
                title=random.choice(TITLES),
                description=random.choice(DESCRIPTIONS),
                price_per_night=round(random.uniform(50, 500), 2),
                max_guests=random.randint(1, 8),
                address=f"{random.randint(1, 999)} Main St",
                city=city,
                country=country,
            )
            listing.save()
            listings.append(listing)

        # ---- Create Bookings for each Listing ----
        for listing in listings:
            check_in = timezone.now().date() + timedelta(days=random.randint(5, 30))
            check_out = check_in + timedelta(days=random.randint(2, 14))
            Booking.objects.create(
                listing=listing,
                guest_name=f"Guest {random.randint(1000, 9999)}",
                guest_email=f"guest{random.randint(1000, 9999)}@example.com",
                check_in=check_in,
                check_out=check_out,
                number_of_guests=random.randint(1, listing.max_guests),
            )

        # ---- Create Reviews for each Listing ----
        for listing in listings:
            for _ in range(random.randint(1, 4)):
                Review.objects.create(
                    listing=listing,
                    author_name=f"Reviewer {random.randint(100, 999)}",
                    rating=random.randint(3, 5),
                    comment=random.choice([
                        "Great stay!", "Highly recommend.", "Lovely host.",
                        "Will come back!", "Perfect location."
                    ])
                )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))