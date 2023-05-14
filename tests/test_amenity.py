import unittest
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    def setUp(self):
        storage.reload()

    def test_save(self):
        """Confirm that the attribute is stored in storage"""

        model = Amenity()

        # save the model to file
        model.save()

    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_creation(self):
        amenity = Amenity(name="Throneville")
        self.assertEqual(amenity.name, "Throneville")

    def test_user_from_dict(self):
        amenity_data = {
            '__class__': 'Amenity',
            'name': 'Throneville'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.name, 'Throneville')


if __name__ == '__main__':
    unittest.main()
