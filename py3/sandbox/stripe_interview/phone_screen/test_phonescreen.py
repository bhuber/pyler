from unittest import TestCase

from stripe_interview.phone_screen.phonescreen import parse_accept_language


class Test(TestCase):
    def test_parse_accept_language(self):
        self.assertEqual(["en-US", "fr-FR"],
                         parse_accept_language(
                             "en-US, fr-CA, fr-FR",  # the client's Accept-Language header, a string
                             ["fr-FR", "en-US"]  # the server's supported languages, a set of strings
                         ))
        self.assertEqual(["en-US", "fr-FR"],
                         parse_accept_language(
                             "en-US,fr-CA,  \tfr-FR",  # the client's Accept-Language header, a string
                             ["fr-FR", "en-US"]  # the server's supported languages, a set of strings
                         ))
        # returns: ["en-US", "fr-FR"]
        self.assertEqual(["fr-FR"], parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]))
        self.assertEqual(["en-US"], parse_accept_language("en-US", ["en-US", "fr-CA"]))
        self.assertEqual([], parse_accept_language("en-US", []))
        self.assertEqual([], parse_accept_language("foo", ["en-US", "fr-CA"]))
        self.assertEqual([], parse_accept_language("", ["en-US", "fr-CA"]))
        self.assertEqual([], parse_accept_language("", []))

    def test_parse_accept_language_unspecific(self):
        self.assertEqual(["en-US"], parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual([], parse_accept_language("en-GB", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["fr-CA", "fr-FR"], parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"]))

        self.assertEqual(["fr-FR", "fr-CA"], parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"]))

    def test_parse_accept_language_wildcard(self):
        self.assertEqual(["en-US", "fr-CA", "fr-FR"],
                         parse_accept_language("en-US, *", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["fr-FR", "fr-CA", "en-US"],
                         parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["fr-FR", "fr-CA", "en-US"],
                         parse_accept_language("fr-FR, fr, *", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["fr-FR", "en-US", "fr-CA"],
                         parse_accept_language("fr-FR, *, fr", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["en-US", "fr-CA", "fr-FR"],
                         parse_accept_language(" * ", ["en-US", "fr-CA", "fr-FR"]))
        self.assertEqual(["en-US", "fr-CA", "fr-FR"],
                         parse_accept_language(" *, ", ["en-US", "fr-CA", "fr-FR"]))

    def test_parse_accept_language_qfactor(self):
        self.assertEqual(["fr-FR", "fr-BG", "fr-CA"], parse_accept_language("fr-FR;q=1, fr-CA;q=0, fr;q=0.5", ["fr-FR", "fr-CA", "fr-BG"]))

        # parse_accept_language("fr-FR;q=1, fr-CA;q=0, *;q=0.5", ["fr-FR", "fr-CA", "fr-BG", "en-US"])
        # returns: ["fr-FR", "fr-BG", "en-US", "fr-CA"]

        # parse_accept_language("en-US;q=1, en;q=0.5, *;q=0", ["en-GB", "en-US", "fr-CA", "fr-FR"])
        # returns: ["en-US", "en-GB", "fr-CA", "fr-FR"]
