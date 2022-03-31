from .base import LANGUAGES, LANGUAGE_CODE

PARLER_LANGUAGES = {
    None: tuple(
        {'code': code}
        for code, name in LANGUAGES
    ),
    'default': {
        'fallbacks': [LANGUAGE_CODE],
        'hide_untranslated': False,
    }
}
