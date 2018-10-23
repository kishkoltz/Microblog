from yandex_translate import YandexTranslate
from flask import current_app
from flask_babel import _
import json

def translate(text, source_language, dest_language):
  # Yandex doesn't require requests (implied?)
  # Yandex doesn't require wrapping key in auth
  # Yandex returns a dict of lists, the translation is found in ['text'][0]
    if 'TRANSLATOR_KEY' not in current_app.config or \
        not current_app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    t = YandexTranslate(current_app.config['TRANSLATOR_KEY'])
    r = t.translate(text, source_language + '-' + dest_language)
    if r['code'] != 200:
        return "Error: the translation service failed. %r" % ( r['code'] )
    return r['text'][0]
