from .base import LANGUAGES, LANGUAGE_CODE, SITE_ID

PARLER_LANGUAGES = {
    SITE_ID: tuple(
        {'code': code}
        for code, name in LANGUAGES
    ),
    'default': {
        'fallbacks': [LANGUAGE_CODE],
        'hide_untranslated': False,
    }
}
