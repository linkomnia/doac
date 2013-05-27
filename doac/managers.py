from django.db import models
from django.db.models.query import QuerySet


class CustomManager(models.Manager):
    """
    Custom manager that adds functionality for the custom query set.
    """
    
    def __getattr__(self, name):
        """
        Forwards methods called on the manager to its query set.
        """
        
        return getattr(self.get_query_set(), name)


class AccessTokenManager(CustomManager):
    
    def get_query_set(self):
        return AccessTokenQuerySet(self.model)


class AccessTokenQuerySet(QuerySet):
    
    def is_active(self):
        return self.filter(is_active=True)


class AuthorizationCodeManager(CustomManager):
    
    def get_query_set(self):
        return AuthorizationCodeQuerySet(self.model)


class AuthorizationCodeQuerySet(QuerySet):
    
    def is_active(self):
        return self.filter(is_active=True)


class AuthorizationTokenManager(CustomManager):
    
    def get_query_set(self):
        return AuthorizationTokenQuerySet(self.model)


class AuthorizationTokenQuerySet(QuerySet):
    
    def is_active(self):
        return self.filter(is_active=True)


class ClientManager(CustomManager):
    
    def get_query_set(self):
        return ClientQuerySet(self.model)


class ClientQuerySet(QuerySet):
    
    def is_active(self):
        return self.filter(is_active=True)


class RedirectUriManager(CustomManager):
    
    def get_query_set(self):
        return RedirectUriQuerySet(self.model)


class RedirectUriQuerySet(QuerySet):
    pass


class RefreshTokenManager(CustomManager):
    
    def get_query_set(self):
        return RefreshTokenQuerySet(self.model)


class RefreshTokenQuerySet(QuerySet):
    
    def is_active(self):
        return self.filter(is_active=True)


class ScopeManager(CustomManager):
    
    def get_query_set(self):
        return ScopeQuerySet(self.model)


class ScopeQuerySet(QuerySet):
    pass
