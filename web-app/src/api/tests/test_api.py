import pytest
from openpyxl import Workbook
import io

from django.urls import reverse


@pytest.fixture
def xlsx_file():
    wb = Workbook()
    ws = wb.active
    codes = [('1144',)]
    for code in codes:
        ws.append(code)
    file = io.BytesIO()
    wb.save(file)
    file.seek(0)
    return file

def test_api_for_vendor_code_input(client):
    expected_data = [{
        'article': 1144,
        'brand': 'Otto',
        'title': 'Otto / Футболка'
    }]
    url = reverse('vendor-code')
    response = client.post(url, data = {'vendor_code': '1144'})
    assert response.status_code == 200
    assert response.data == expected_data


def test_api_for_xlsx_input(client, xlsx_file):
    expected_data = [{
        'article': 1144,
        'brand': 'Otto',
        'title': 'Otto / Футболка'
    }]
    url = reverse('vendor-code')
    response = client.post(url, data = {'vendor_code_file': xlsx_file}, format='multipart')
    assert response.status_code == 200
    assert response.data == expected_data
