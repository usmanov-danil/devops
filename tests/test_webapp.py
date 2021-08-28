from datetime import datetime
from unittest import TestCase

import pytest
import pytz

from app_python.app import app


class TestApp(TestCase):
    def setUp(self) -> None:
        self.client = app.test_client(self)

    def test_correct_url(self):
        response = self.client.get('/')
        assert response.status_code == 200

    def test_incorrect_url(self):
        response = self.client.get('/unknow_endpoint/')
        assert response.status_code == 404

    @pytest.mark.freeze_time
    def test_time(self):
        now = datetime.now(tz=pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
        response = self.client.get('/')

        assert now in response.data.decode('utf-8')
