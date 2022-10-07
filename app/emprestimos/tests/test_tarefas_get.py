import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def response(client):
    return client.get(reverse('emprestimos:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_present_form(response):
    assertContains(response, '<form')


def test_button_submit_form(response):
    assertContains(response, '<button type="submit"')
