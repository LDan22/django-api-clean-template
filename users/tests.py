"""Users app tests"""

import pytest
from django.conf import settings
from django.contrib.auth import get_user_model


@pytest.fixture(scope="session")
def django_db_setup():
    """
    Setup for test database
    """
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": settings.SQL_DATABASE,
        "USER": settings.SQL_USER,
        "PASSWORD": settings.SQL_PASSWORD,
        "HOST": settings.SQL_HOST,
        "PORT": settings.SQL_PORT,
    }


@pytest.fixture
def db_access_without_rollback_and_truncate(request, django_db_blocker):
    """
    Check database access
    """
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)


@pytest.mark.django_db
def test_user_create():
    """
    Test user creation success
    """
    get_user_model().objects.create_user(
        "john", "lennon@thebeatles.com", "johnpassword"
    )
    assert get_user_model().objects.count() == 1
