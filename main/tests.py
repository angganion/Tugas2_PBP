from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_page_content(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Wahyu Ridho Anggoro')

    def test_main_page_status_code(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)
    
    def test_main_page_links(self):
        response = Client().get('/main/')
        self.assertContains(response, '''<a href='https://youtu.be/xvFZjo5PgG0?si=JZ-ebX8f-Ef07mmZ'> <img src="https://i.postimg.cc/d0BS4khx/Mega-Jackpot-Merah-Klikhoki.gif"></a>''')

    def test_create_item(self):
        item = Item.objects.create(
            name='Barang Baru',
            amount=100,
            description='Deskripsi Barang',
            rarity=3
        )

        # Periksa apakah objek Item telah terbuat dengan benar
        self.assertEqual(item.name, 'Barang Baru')
        self.assertEqual(item.amount, 100)
        self.assertEqual(item.description, 'Deskripsi Barang')
        self.assertEqual(item.rarity, 3)


