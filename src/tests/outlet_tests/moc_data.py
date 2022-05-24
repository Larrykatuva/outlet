import os
from django.conf import settings


class MockData:

    def __init__(self):
        self.outlet_data = {
            "name": "Charleen",
            "location": "Trust Building Moi Avenue Shop-15",
            "latitude": "1234.45",
            "longitude": "1234.45",
            "image": open(os.path.join(settings.BASE_DIR, 'fb.jpeg'), encoding="utf8", errors='ignore')
        }
