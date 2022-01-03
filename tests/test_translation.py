import unittest
import owlapp.translation as transl


class TestTranslation(unittest.TestCase):
    def test_detect_lang(self):
        eng = transl.detect_language('Hello I am Tom')
        self.assertEqual(eng , 'en')


    def test_translate(self):
        eng = transl.translate_text('fr','Hello')
        self.assertEqual(eng, 'Bonjour')
