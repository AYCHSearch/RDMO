from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import RequestContext, Template
from django.test.client import RequestFactory
from django.utils import translation


class CoreTestCase(TestCase):

    fixtures = (
        'auth.json',
        'accounts.json',
    )


class CoreTests(CoreTestCase):

    def setUp(self):
        translation.activate('en')

    def test_home_view(self):
        """ The home page can be accessed. """

        # test as AnonymousUser
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # test as regular user
        self.client.login(username='user', password='user')
        response = self.client.get('/')
        self.assertRedirects(response, reverse('projects'))

        # test as manager
        self.client.login(username='manager', password='manager')
        response = self.client.get('/')
        self.assertRedirects(response, reverse('projects'))

        # test as admin
        self.client.login(username='admin', password='admin')
        response = self.client.get('/')
        self.assertRedirects(response, reverse('projects'))

    def test_i18n_switcher(self):
        ''' The i18n switcher works. '''

        # get the url to switch to german
        url = reverse('i18n_switcher', args=['de'])

        # switch to german and check if the header is there
        response = self.client.get(url, HTTP_REFERER='http://testserver/')
        self.assertEqual(302, response.status_code)
        self.assertIn('de', response['Content-Language'])

        # get the url to switch to english
        url = reverse('i18n_switcher', args=['en'])

        # switch to german and check if the header is there
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        self.assertIn('en', response['Content-Language'])


class CoreTagsTests(TestCase):
    def setUp(self):
        self.request = RequestFactory().get('/')

    def test_i18n_switcher(self):
        """ The language switcher is rendered correctly. """

        # create a fake template with a name
        template = "{% load core_tags %}{% i18n_switcher %}"

        # set a language
        translation.activate(settings.LANGUAGES[0][0])

        # render the link
        context = RequestContext(self.request, {})
        rendered_template = Template(template).render(context)
        for language in settings.LANGUAGES:
            if language == settings.LANGUAGES[0]:
                self.assertIn('<a href="/i18n/%s/"><u>%s</u></a>' % language, rendered_template)
            else:
                self.assertIn('<a href="/i18n/%s/">%s</a>' % language, rendered_template)
