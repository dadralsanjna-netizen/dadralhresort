import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
django.setup()

from app1.models import Gallery
from django.core.files.base import ContentFile
import requests

def add_sample_gallery_items():
    # Sample gallery items
    items = [
        {
            'title': 'Luxury Suite',
            'description': 'Experience unparalleled luxury in our signature suite',
            'image_url': 'https://images.unsplash.com/photo-1590490360182-c33d57733427',
            'price': 599.99
        },
        {
            'title': 'Royal Pool Villa',
            'description': 'Private villa with infinity pool and stunning views',
            'image_url': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b',
            'price': 899.99
        },
        {
            'title': 'Garden Courtyard',
            'description': 'Serene garden spaces perfect for relaxation',
            'image_url': 'https://images.unsplash.com/photo-1566665797739-1674de7a421a',
            'price': 299.99
        },
        {
            'title': 'Presidential Suite',
            'description': 'The epitome of luxury with panoramic views',
            'image_url': 'https://images.unsplash.com/photo-1578683010236-d716f9a3f461',
            'price': 1299.99
        }
    ]

    for item in items:
        try:
            # Download image from URL
            response = requests.get(item['image_url'])
            if response.status_code == 200:
                # Create gallery item
                gallery_item = Gallery(
                    title=item['title'],
                    description=item['description'],
                    price=item['price']
                )
                
                # Save image
                image_name = f"gallery_{item['title'].lower().replace(' ', '_')}.jpg"
                gallery_item.image.save(
                    image_name,
                    ContentFile(response.content),
                    save=True
                )
                
                print(f"Created gallery item: {item['title']}")
            else:
                print(f"Failed to download image for {item['title']}")
        except Exception as e:
            print(f"Error creating gallery item {item['title']}: {str(e)}")

if __name__ == '__main__':
    print("Adding sample gallery items...")
    add_sample_gallery_items()
    print("Done!")