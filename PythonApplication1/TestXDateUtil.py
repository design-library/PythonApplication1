# coding: utf-8
import traceback
import unittest

from datetime import datetime

from util.XDateUtil import XDateUtil

class TestXDateUtil(unittest.TestCase):

    '''
    ユニットテスト 
    '''

    xDateUtil = XDateUtil()

    def setUp(self):
        ''' setUp '''


    def test_to_ad_m_34_6_29(self):

        # 明治x年6月29日
        with self.assertRaises(Exception):
            self.xDateUtil.to_ad('明治', 34, 6, 29)


    def test_to_ad_t_1_7_30(self):

        # 大正1年7月30日
        # {'yyyy': 1989, 'MM': 1, 'dd': 7}
        print(self.xDateUtil.to_ad('大正', 1, 7, 30))
        self.assertEqual(
            {'yyyy': 1912, 'MM': 7, 'dd': 30}, 
            self.xDateUtil.to_ad('大正', 1, 7, 30))


    def test_to_ad_t_15_12_24(self):

        # 大正15年12月24日
        # {'yyyy': 1926, 'MM': 12, 'dd': 24}
        print(self.xDateUtil.to_ad('大正', 15, 12, 24))
        self.assertEqual(
            {'yyyy': 1926, 'MM': 12, 'dd': 24}, 
            self.xDateUtil.to_ad('大正', 15, 12, 24))


    def test_to_ad_s_1_12_25(self):

        # 昭和1年12月25日
        # {'yyyy': 1926, 'MM': 12, 'dd': 25}
        print(self.xDateUtil.to_ad('昭和', 1, 12, 25))
        self.assertEqual(
            {'yyyy': 1926, 'MM': 12, 'dd': 25}, 
            self.xDateUtil.to_ad('昭和', 1, 12, 25))


    def test_to_ad_s_64_1_7(self):

        # 昭和64年1月7日
        # {'yyyy': 1989, 'MM': 1, 'dd': 7}
        print(self.xDateUtil.to_ad('昭和', 64, 1, 7))
        self.assertEqual(
            {'yyyy': 1989, 'MM': 1, 'dd': 7}, 
            self.xDateUtil.to_ad('昭和', 64, 1, 7))


    def test_to_ad_h_1_1_8(self):

        # 平成1年1月8日
        #{'yyyy': 1989, 'MM': 1, 'dd': 8}
        print(self.xDateUtil.to_ad('平成', 1, 1, 8))
        self.assertEqual(
            {'yyyy': 1989, 'MM': 1, 'dd': 8}, 
            self.xDateUtil.to_ad('平成', 1, 1, 8))


    def test_to_ad_h_31_4_30(self):

        # 平成31年4月30日
        #{'yyyy': 2019, 'MM': 4, 'dd': 30}
        print(self.xDateUtil.to_ad('平成', 31, 4, 30))
        self.assertEqual(
            {'yyyy': 2019, 'MM': 4, 'dd': 30}, 
            self.xDateUtil.to_ad('平成', 31, 4, 30))


    def test_to_ad_r_1_5_1(self):

        # 令和1年5月1日
        #{'yyyy': 2019, 'MM': 5, 'dd': 1}
        print(self.xDateUtil.to_ad('令和', 1, 5, 1))
        self.assertEqual(
            {'yyyy': 2019, 'MM': 5, 'dd': 1}, 
            self.xDateUtil.to_ad('令和', 1, 5, 1))


    def test_to_jc_1989_1_7(self):

        # 1989年1月7日
        #{'era_code': 1, 'era_ab': 'S', 'era': '昭和', 'yy': 64, 'MM': 1, 'dd': 7}
        print(self.xDateUtil.to_jc(1989, 1, 7))
        self.assertEqual(
            {'era_code': 1, 'era_ab': 'S', 'era': '昭和', 'yy': 64, 'MM': 1, 'dd': 7},
            self.xDateUtil.to_jc(1989, 1, 7))


    def test_to_jc_1989_1_8(self):

        # 1989年1月8日
        #{'era_code': 2, 'era_ab': 'H', 'era': '平成', 'yy': 1, 'MM': 1, 'dd': 8}
        print(self.xDateUtil.to_jc(1989, 1, 8))
        self.assertEqual(
            {'era_code': 2, 'era_ab': 'H', 'era': '平成', 'yy': 1, 'MM': 1, 'dd': 8},
            self.xDateUtil.to_jc(1989, 1, 8))


    def test_to_jc_2019_4_30(self):

        # 2019年4月30日
        #{'era_code': 2, 'era_ab': 'H', 'era': '平成', 'yy': 31, 'MM': 4, 'dd': 30}
        print(self.xDateUtil.to_jc(2019, 4, 30))
        self.assertEqual(
            {'era_code': 2, 'era_ab': 'H', 'era': '平成', 'yy': 31, 'MM': 4, 'dd': 30},
            self.xDateUtil.to_jc(2019, 4, 30))


    def test_to_jc_2019_5_1(self):

        # 2019年5月1日
        #{'era_code': 3, 'era_ab': 'R', 'era': '令和', 'yy': 1, 'MM': 5, 'dd': 1}
        print(self.xDateUtil.to_jc(2019, 5, 1))
        self.assertEqual(
            {'era_code': 3, 'era_ab': 'R', 'era': '令和', 'yy': 1, 'MM': 5, 'dd': 1},
            self.xDateUtil.to_jc(2019, 5, 1))


if __name__ == "__main__":
    unittest.main()
