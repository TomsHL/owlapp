from google.cloud import translate_v2 as translate
import six


def detect_language(text):
    """Detects the text's language."""

    translate_client = translate.Client()
    result = translate_client.detect_language(text)
    return result["language"]


def translate_text(target, text):
    """Translates text into the target language."""

    translate_client = translate.Client()
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    return result['translatedText']
