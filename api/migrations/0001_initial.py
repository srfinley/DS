# Generated by Django 3.0.1 on 2019-12-22 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airbnb',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('listing_url', models.TextField(default='')),
                ('scrape_id', models.TextField(default='')),
                ('last_scraped', models.TextField(default='')),
                ('name', models.TextField(default='')),
                ('summary', models.TextField(default='')),
                ('space', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('experiences_offered', models.TextField(default='')),
                ('neighborhood_overview', models.TextField(default='')),
                ('notes', models.TextField(default='')),
                ('transit', models.TextField(default='')),
                ('access', models.TextField(default='')),
                ('interaction', models.TextField(default='')),
                ('house_rules', models.TextField(default='')),
                ('thumbnail_url', models.TextField(default='')),
                ('medium_url', models.TextField(default='')),
                ('picture_url', models.TextField(default='')),
                ('xl_picture_url', models.TextField(default='')),
                ('host_id', models.TextField(default='')),
                ('host_url', models.TextField(default='')),
                ('host_name', models.TextField(default='')),
                ('host_since', models.TextField(default='')),
                ('host_location', models.TextField(default='')),
                ('host_about', models.TextField(default='')),
                ('host_response_time', models.TextField(default='')),
                ('host_response_rate', models.TextField(default='')),
                ('host_acceptance_rate', models.TextField(default='')),
                ('host_is_superhost', models.TextField(default='')),
                ('host_thumbnail_url', models.TextField(default='')),
                ('host_picture_url', models.TextField(default='')),
                ('host_neighbourhood', models.TextField(default='')),
                ('host_listings_count', models.TextField(default='')),
                ('host_total_listings_count', models.TextField(default='')),
                ('host_verifications', models.TextField(default='')),
                ('host_has_profile_pic', models.TextField(default='')),
                ('host_identity_verified', models.TextField(default='')),
                ('street', models.TextField(default='')),
                ('neighbourhood', models.TextField(default='')),
                ('neighbourhood_cleansed', models.TextField(default='')),
                ('neighbourhood_group_cleansed', models.TextField(default='')),
                ('city', models.TextField(default='')),
                ('state', models.TextField(default='')),
                ('zipcode', models.TextField(default='')),
                ('market', models.TextField(default='')),
                ('smart_location', models.TextField(default='')),
                ('country_code', models.TextField(default='')),
                ('country', models.TextField(default='')),
                ('latitude', models.TextField(default='')),
                ('longitude', models.TextField(default='')),
                ('is_location_exact', models.TextField(default='')),
                ('property_type', models.TextField(default='')),
                ('room_type', models.TextField(default='')),
                ('accommodates', models.TextField(default='')),
                ('bathrooms', models.TextField(default='')),
                ('bedrooms', models.TextField(default='')),
                ('beds', models.TextField(default='')),
                ('bed_type', models.TextField(default='')),
                ('amenities', models.TextField(default='')),
                ('square_feet', models.TextField(default='')),
                ('price', models.TextField(default='')),
                ('weekly_price', models.TextField(default='')),
                ('monthly_price', models.TextField(default='')),
                ('security_deposit', models.TextField(default='')),
                ('cleaning_fee', models.TextField(default='')),
                ('guests_included', models.TextField(default='')),
                ('extra_people', models.TextField(default='')),
                ('minimum_nights', models.TextField(default='')),
                ('maximum_nights', models.TextField(default='')),
                ('minimum_minimum_nights', models.TextField(default='')),
                ('maximum_minimum_nights', models.TextField(default='')),
                ('minimum_maximum_nights', models.TextField(default='')),
                ('maximum_maximum_nights', models.TextField(default='')),
                ('minimum_nights_avg_ntm', models.TextField(default='')),
                ('maximum_nights_avg_ntm', models.TextField(default='')),
                ('calendar_updated', models.TextField(default='')),
                ('has_availability', models.TextField(default='')),
                ('availability_30', models.TextField(default='')),
                ('availability_60', models.TextField(default='')),
                ('availability_90', models.TextField(default='')),
                ('availability_365', models.TextField(default='')),
                ('calendar_last_scraped', models.TextField(default='')),
                ('number_of_reviews', models.TextField(default='')),
                ('number_of_reviews_ltm', models.TextField(default='')),
                ('first_review', models.TextField(default='')),
                ('last_review', models.TextField(default='')),
                ('review_scores_rating', models.TextField(default='')),
                ('review_scores_accuracy', models.TextField(default='')),
                ('review_scores_cleanliness', models.TextField(default='')),
                ('review_scores_checkin', models.TextField(default='')),
                ('review_scores_communication', models.TextField(default='')),
                ('review_scores_location', models.TextField(default='')),
                ('review_scores_value', models.TextField(default='')),
                ('requires_license', models.TextField(default='')),
                ('license', models.TextField(default='')),
                ('jurisdiction_names', models.TextField(default='')),
                ('instant_bookable', models.TextField(default='')),
                ('is_business_travel_ready', models.TextField(default='')),
                ('cancellation_policy', models.TextField(default='')),
                ('require_guest_profile_picture', models.TextField(default='')),
                ('require_guest_phone_verification', models.TextField(default='')),
                ('calculated_host_listings_count', models.TextField(default='')),
                ('calculated_host_listings_count_entire_homes', models.TextField(default='')),
                ('calculated_host_listings_count_private_rooms', models.TextField(default='')),
                ('calculated_host_listings_count_shared_rooms', models.TextField(default='')),
                ('reviews_per_month', models.TextField(default='')),
            ],
        ),
    ]