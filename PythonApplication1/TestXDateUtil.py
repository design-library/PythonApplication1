# coding: utf-8
import unittest

from datetime import datetime

import XDateUtil

class TestXDateUtil(unittest.TestCase):
    ''' ユニットテスト '''

    def setUp(self):
        ''' setUp '''


    def test_toAd(self):
        ''' toAd test. '''

        print XDateUtil.toAd('平成', '26', '8', '2')
