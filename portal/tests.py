from django.test import TestCase
from django.utils import timezone
from .models import Campaign, Event


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get('/')

        self.assertContains(response, 'Bem-vindo ao nosso portal!')
        self.assertContains(response, 'Nossas campanhas')
        self.assertContains(response, 'Próximos eventos')

    def test_about_page_status_code(self):
        response = self.client.get('/sobre/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contato/')
        self.assertEqual(response.status_code, 200)

    def test_adoption_page_status_code(self):
        response = self.client.get('/adocao/')
        self.assertEqual(response.status_code, 200)

    def test_how_to_help_page_status_code(self):
        response = self.client.get('/como-ajudar/')
        self.assertEqual(response.status_code, 200)


class CampaignModelTest(TestCase):

    def test_create_campaign(self):
        campaign = Campaign.objects.create(
            title='Campanha de Teste',
            description='Descrição da campanha.'
        )

        self.assertEqual(campaign.title, 'Campanha de Teste')
        self.assertTrue(campaign.is_active)

    def test_campaign_string_representation(self):
        campaign = Campaign.objects.create(
            title='Campanha de Ração',
            description='Arrecadação de ração.'
        )

        self.assertEqual(str(campaign), 'Campanha de Ração')


class EventModelTest(TestCase):

    def test_create_event(self):
        event = Event.objects.create(
            title='Feira de Adoção',
            description='Evento de adoção responsável.',
            date=timezone.now(),
            location='Porto Alegre, RS'
        )

        self.assertEqual(event.title, 'Feira de Adoção')
        self.assertTrue(event.is_active)

    def test_event_string_representation(self):
        event = Event.objects.create(
            title='Feira de Adoção',
            description='Evento de adoção responsável.',
            date=timezone.now(),
            location='Porto Alegre, RS'
        )

        self.assertEqual(str(event), 'Feira de Adoção')