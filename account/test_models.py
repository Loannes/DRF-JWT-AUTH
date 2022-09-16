from django.test import TestCase
from unittest import mock
from datetime import datetime

from .models import User

# https://dev-yakuza.posstree.com/ko/django/test/models/
# python manage.py test
# 테스트 해야 하는 항목
#   포스트의 제목에 최대값이 100자라면 100자가 넘어가면 오류가 발생하는가?
#   

class UserModelTest(TestCase):
    def test_default_values(self):
        mock_date = datetime(2022, 9, 16, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            user = User.objects.create(email='test@test.test', password='12345', date_of_birth='2000-01-01')

        self.assertEquals(user.email, 'test@test.test')
        self.assertEquals(user.is_active, True)
        self.assertEquals(user.is_admin, False)
        self.assertEquals(user.date_of_birth, '2000-01-01')
        # self.assertEquals(user.created_at, mock_date)
        # self.assertEquals(user.updated_at, mock_date)

    def test_not_birth_date(TestCate):
        mock_date = datetime(2022, 9, 16, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
            user = User.objects.create(email='test@test.test', password='12345')

    # def test_updated_at(self):
    #     mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
    #     with mock.patch('django.utils.timezone.now') as mock_now:
    #         mock_now.return_value = mock_date
    #         user = User.objects.create(email='test@test.test', password='12345')

    #     self.assertEquals(user.created_at, mock_date)
    #     self.assertEquals(user.updated_at, mock_date)
    #     self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-04')

    #     mock_update_date = datetime(2021, 3, 5, 14, 57, 11, 703055)
    #     with mock.patch('django.utils.timezone.now') as mock_now:
    #         mock_now.return_value = mock_update_date
    #         user.is_admin = True
    #         user.save()

    #     self.assertEquals(user.created_at, mock_date)
    #     self.assertEquals(user.updated_at, mock_update_date)
    #     self.assertEquals(user.updated_at.strftime("%Y-%m-%d"), '2021-03-05')