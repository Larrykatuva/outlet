import os
from django.conf import settings


class MockData:

    def __init__(self):

        self.profile_data1 = {
            "image": open(os.path.join(settings.BASE_DIR, 'fb.jpeg'), encoding="utf8", errors='ignore'),
            "first_name": "Lawrence",
            "last_name": "Katuva",
            "phone": "0720460519",
            "date_of_birth": "1998-08-15",
            "gender": "Male"
        }
