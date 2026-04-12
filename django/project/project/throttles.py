from rest_framework.throttling import AnonRateThrottle

class LoginAnonRateThrottle(AnonRateThrottle):
    scope = 'login'

class RegisterAnonRateThrottle(AnonRateThrottle):
    scope = 'register'