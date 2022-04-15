import environ

env = environ.FileAwareEnv()
DEVELOPMENT = env.bool("DEVELOPMENT", default=True)

if DEVELOPMENT:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    BASE_BACKEND = EMAIL_BACKEND
else:
    EMAIL_BACKEND = "cl.lib.email_backends.EmailBackend"
    BASE_BACKEND = "django_ses.SESBackend"
    AWS_SES_REGION_NAME = "us-west-2"
    AWS_SES_REGION_ENDPOINT = "email.us-west-2.amazonaws.com"

# Max email attachment to send in bytes, 350KB
MAX_ATTACHMENT_SIZE = 350_000

# 1: Every message is BCC'ed
# 0.5: Half of messages are BCC'ed
# 0.1: 10% of messages are BCC'ed
# 0: No messages are BCC'ed
EMAIL_BCC_COPY_RATE = 0.1

BCC_EMAIL_ADDRESS = "bcc@free.law"

SERVER_EMAIL = "CourtListener <noreply@courtlistener.com>"
DEFAULT_FROM_EMAIL = "CourtListener <noreply@courtlistener.com>"
DEFAULT_ALERTS_EMAIL = "CourtListener Alerts <alerts@courtlistener.com>"
SCRAPER_ADMINS = (
    ("Slack Juriscraper Channel", "j9f4b5n5x7k8x2r1@flp-talk.slack.com"),
    ("PA", "arderyp@protonmail.com"),
)