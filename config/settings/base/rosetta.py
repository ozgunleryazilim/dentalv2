from .base import LANGUAGES, LANGUAGE_CODE

# ROSETTA_MESSAGES_PER_PAGE = 20
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = False
ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = LANGUAGE_CODE
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = list(filter(lambda x: x[0] == LANGUAGE_CODE, LANGUAGES))[0][1]
ROSETTA_WSGI_AUTO_RELOAD = ROSETTA_UWSGI_AUTO_RELOAD = True
ROSETTA_SHOW_AT_ADMIN_PANEL = True
