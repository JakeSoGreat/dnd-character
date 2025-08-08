from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Character, Race, Background, Alignment, Class
from .forms import CharacterForm

class CharacterModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create required related objects
        self.race = Race.objects.create(name='Human')
        self.background = Background.objects.create(name='Noble')
        self.alignment = Alignment.objects.create(name='Lawful Good')
        self.character_class = Class.objects.create(name='Fighter')
        
        self.character = Character.objects.create(
            name='Test Character',
            level=5,
            user=self.user,
            race=self.race,
            background=self.background,
            alignment=self.alignment,
            strength=15,
            dexterity=14,
            constitution=13,
            intelligence=12,
            wisdom=10,
            charisma=8
        )
        self.character.character_classes.add(self.character_class)

    def test_character_creation(self):
        """Test character model creation"""
        self.assertEqual(self.character.name, 'Test Character')
        self.assertEqual(self.character.level, 5)
        self.assertEqual(self.character.user, self.user)
        self.assertEqual(str(self.character), 'Test Character')

    def test_character_level_validation(self):
        """Test character level constraints"""
        # Test valid level
        self.character.level = 10
        self.character.full_clean()  # Should not raise ValidationError
        
        # Test invalid level (you'll need to add validation to your model)
        self.character.level = 25
        with self.assertRaises(Exception):
            self.character.full_clean()


class CharacterViewTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create required related objects
        self.race = Race.objects.create(name='Human')
        self.background = Background.objects.create(name='Noble')
        self.alignment = Alignment.objects.create(name='Lawful Good')
        self.character_class = Class.objects.create(name='Fighter')

    def test_character_list_requires_login(self):
        """Test that character list requires authentication"""
        response = self.client.get(reverse('character_list'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_character_list_authenticated(self):
        """Test character list for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('character_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your Characters')

    def test_character_create_get(self):
        """Test character create form display"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('character_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Character')

    def test_character_create_post(self):
        """Test character creation via POST"""
        self.client.login(username='testuser', password='testpass123')
        data = {
            'name': 'New Character',
            'level': 3,
            'race': self.race.id,
            'background': self.background.id,
            'alignment': self.alignment.id,
            'strength': 15,
            'dexterity': 14,
            'constitution': 13,
            'intelligence': 12,
            'wisdom': 10,
            'charisma': 8,
            'character_classes': [self.character_class.id],
        }
        response = self.client.post(reverse('character_create'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Character.objects.filter(name='New Character').exists())


class CharacterFormTest(TestCase):
    def setUp(self):
        """Set up test data"""
        self.race = Race.objects.create(name='Human')
        self.background = Background.objects.create(name='Noble')
        self.alignment = Alignment.objects.create(name='Lawful Good')
        self.character_class = Class.objects.create(name='Fighter')

    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'name': 'Test Character',
            'level': 5,
            'race': self.race.id,
            'background': self.background.id,
            'alignment': self.alignment.id,
            'strength': 15,
            'dexterity': 14,
            'constitution': 13,
            'intelligence': 12,
            'wisdom': 10,
            'charisma': 8,
            'character_classes': [self.character_class.id],
        }
        form = CharacterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_level(self):
        """Test form with invalid level"""
        form_data = {
            'name': 'Test Character',
            'level': 25,  # Invalid level
            'race': self.race.id,
            'background': self.background.id,
            'alignment': self.alignment.id,
            'strength': 15,
            'dexterity': 14,
            'constitution': 13,
            'intelligence': 12,
            'wisdom': 10,
            'charisma': 8,
            'character_classes': [self.character_class.id],
        }
        form = CharacterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('level', form.errors)


class AuthViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page(self):
        """Test login page loads"""
        response = self.client.get(reverse('custom_login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_register_page(self):
        """Test register page loads"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_home_page(self):
        """Test home page loads"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
