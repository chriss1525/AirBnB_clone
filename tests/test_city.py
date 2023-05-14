import unittest
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    def setUp(self):
        storage.reload()

    def test_save_(self):
        """Confirm that the attribute is stored in storage"""

        model = City()

        # save the model to file
        model.save()

    def test_city_creation(self):
        city = City(id="123", name="Doe")
        self.assertEqual(city.id, "123")
        self.assertEqual(city.name, "Doe")

    def test_city_to_dict(self):
        city = City(id="123", name="Doe")
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], '123')
        self.assertEqual(city_dict['name'], 'Doe')

    def test_city_from_dict(self):
        city_data = {
            '__class__': 'City',
            'id': '123',
            'name': 'Doe'
        }
        city = City(**city_data)
        self.assertEqual(city.id, '123')
        self.assertEqual(city.name, 'Doe')


if __name__ == '__main__':
    unittest.main()
