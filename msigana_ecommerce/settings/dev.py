from .base import *
from decouple import  config


DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV').split(',')
SECRET_KEY = config('SECRET_KEY')




# Appication definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'category.apps.CategoryConfig',
    'store.apps.StoreConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'heads.apps.HeadsConfig',
    'blog.apps.BlogConfig', 
    'footer.apps.FooterConfig',
    'contact.apps.ContactConfig',
    'advertizement.apps.AdvertizementConfig',
    'telebirrpay.apps.TelebirrpayConfig',
    'rewardpay.apps.RewardpayConfig',
    'bankpay.apps.BankpayConfig',
    'reservations.apps.ReservationsConfig',
    'catering.apps.CateringConfig',
    'menu.apps.MenuConfig',
    'happening.apps.HappeningConfig',
    'gallery.apps.GalleryConfig',
   'video_gallery.apps.VideoGalleryConfig',
   'main_video.apps.MainVideoConfig',
    'nested_admin',
    'tailwind',
    'theme',
    'django_quill',
    'django_browser_reload',
    'rest_framework',
  
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DEV_DATABASE_NAME'),
        'USER': config('DEV_DATABASE_USER'),
        'PASSWORD': config('DEV_DATABASE_PASSWORD'),
        'HOST': config('DEV_DATABASE_HOST'),
        'PORT': config('DEV_DATABASE_PORT'),
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.henomrestaurant.com' 
EMAIL_PORT = 465  
EMAIL_USE_SSL = True  
EMAIL_USE_TLS = False  
EMAIL_HOST_USER = 'info@henomrestaurant.com'  
EMAIL_HOST_PASSWORD = 'henomrestauranT11@#'  
DEFAULT_FROM_EMAIL = 'info@henomrestaurant.com'  
ADMIN_EMAIL = 'info@henomrestaurant.com'  