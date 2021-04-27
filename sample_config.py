HEROKU = True   # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(environ["SUDO_CHAT_ID"])
    OWNER_ID = int(environ["OWNER_ID"])
    SESSION_STRING = environ["SESSION_STRING"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 4167120
    API_HASH = "03253da188b3dbe1a94ba32c2d7091af"
    SUDO_CHAT_ID = -1001228152183
    OWNER_ID = 656329268


# don't make changes below this line
ARQ_API = "http://35.240.133.234:8000"
