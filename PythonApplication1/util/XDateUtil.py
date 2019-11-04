# coding: utf-8

from datetime import datetime
from datetime import date

class XDateUtil():

    ''' 
    共通業務部品日付クラス

    Attributes
    ----------
    _JC_T_DICT : dict
        和暦大正の辞書。

    _JC_S_DICT : dict
        和暦昭和の辞書。

    _JC_H_DICT : dict
        和暦平成の辞書。

    _JC_R_DICT : dict
        和暦令和の辞書。

    _JC_LIST : list
        和暦辞書リスト。

    Notes
    ----------
    和暦辞書は以下の形式となる。
    {'ERA_CODE':元号コード, 
     'ERA_AB'  :元号略称, 
     'ERA'     :元号, 
     'FROM'    :開始年月日datetime(yyyy,yy,mm), 
     'TO'      :終了年月日datetime(yyyy,yy,mm)}

    和暦辞書リストは以下の形式となる。
    [和暦大正の辞書, 和暦昭和の辞書, 和暦平成の辞書, 和暦令和の辞書]

    '''

    _JC_T_DICT = {'ERA_CODE':0, 
                  'ERA_AB'  :'T', 
                  'ERA'     :'大正', 
                  'FROM':datetime(1912, 7, 30), 
                  'TO'  :datetime(1926, 12, 24)}

    _JC_S_DICT = {'ERA_CODE':1, 
                  'ERA_AB'  :'S', 
                  'ERA'     :'昭和', 
                  'FROM':datetime(1926, 12, 25), 
                  'TO'  :datetime(1989, 1, 7)}

    _JC_H_DICT = {'ERA_CODE':2, 
                  'ERA_AB'  :'H', 
                  'ERA'     :'平成', 
                  'FROM':datetime(1989, 1, 8), 
                  'TO'  :datetime(2019, 4, 30)}

    _JC_R_DICT = {'ERA_CODE':3, 
                  'ERA_AB':'R', 
                  'ERA':'令和', 
                  'FROM':datetime(2019, 5, 1), 
                  'TO'  :datetime.today()}

    _JC_LIST = [_JC_T_DICT, _JC_S_DICT, _JC_H_DICT, _JC_R_DICT]


    def __init__(self):
        ''' コンストラクタ '''


    def to_ad(self, p_jc, p_yy, p_mm, p_dd):
    
        ''' 
        和暦から西暦に変換する。
        
        Parameters
        ----------
        p_jc : string
            元号（大正、昭和、平成、令和）
        p_yy : int
            年（yy）
        p_mm : int
            月（mm）
        p_dd : int
            日（dd）
            
        Returns
        ----------
        {'yyyy':yyyy, 'MM':mm, 'dd':dd} : dect
            西暦辞書

        Raises
        ----------
        Exception
            和暦から西暦に変換できない場合、例外を投げる。

        '''
        
        yy = int(p_yy)
        mm = int(p_mm)
        dd = int(p_dd)
        for _jc_dict in self._JC_LIST:
            if p_jc == _jc_dict['ERA']:
                # 該当元号の開始年月日と終了年月日
                from_date = _jc_dict['FROM']
                to_date   = _jc_dict['TO']

                # 西暦変換
                today = datetime.today()
                if today == _jc_dict['TO']:
                    # 現在の西暦年を西暦年とする
                    year = datetime.today.year
                    yyyy = int(year)
                    # 終了年月日を現在の西暦年月日とする
                    to_date   = today

                else:
                    # 和暦年から西暦年の計算
                    year = int(_jc_dict['FROM'].year)
                    yyyy = int(self. _calc_ad(yy, year))
                
                # 妥当性チェック
                if self.is_date(yyyy, p_mm, p_dd):
                    target_date = datetime(yyyy, mm, dd)

                    if from_date <= target_date <= to_date:
                        return {'yyyy':yyyy, 'MM':mm, 'dd':dd}
                    
        raise Exception


    def to_jc(self, p_yyyy, p_mm):
    
        ''' 
        西暦から和暦に変換する。
        
        Parameters
        ----------
        p_yyyy : int
            年（yyyy）
        p_mm : int
            月（mm）
            
        Returns
        ----------
        {'era_code':era_code, 
         'era_ab'  :era_ab, 
         'era'     :era, 
         'yy':yy, 'MM':mm, 'dd':dd} : dect
            和暦辞書（※'dd'は月末日が格納される）

        Raises
        ----------
        Exception
            西暦から和暦に変換できない場合、例外を投げる。
        '''
        
        yyyy = int(p_yyyy)
        mm = int(p_mm)
        dd = int(datetime.date(yyyy, mm + 1, 1) - datetime.timedelta(days=1))

        jc_dict = self.to_jc(yyyy, mm, dd)

        return jc_dict


    def to_jc(self, p_yyyy, p_mm, p_dd):
    
        ''' 
        西暦から和暦に変換する。
        
        Parameters
        ----------
        p_yyyy : int
            年（yyyy）
        p_mm : int
            月（mm）
        p_dd : int
            日（dd）
            
        Returns
        ----------
        {'era_code':era_code, 
         'era_ab'  :era_ab, 
         'era'     :era, 
         'yy':yy, 'MM':mm, 'dd':dd} : dect
            和暦辞書

        Raises
        ----------
        Exception
            西暦から和暦に変換できない場合、例外を投げる。
        '''
        
        yyyy = int(p_yyyy)
        mm = int(p_mm)
        dd = int(p_dd)
        for _jc_dict in self._JC_LIST:

            # 妥当性チェック
            if self.is_date(yyyy, p_mm, p_dd):

                target_date = datetime(yyyy, mm, dd)
                from_date = _jc_dict['FROM']
                to_date   = _jc_dict['TO']

                if from_date <= target_date <= to_date:
                    # 西暦から和暦変換の計算処理
                    year = int(_jc_dict['FROM'].year)
                    yy = int(self._calc_jc(yyyy, year))

                    return {'era_code':_jc_dict['ERA_CODE'], 
                     'era_ab'  :_jc_dict['ERA_AB'], 
                     'era'     :_jc_dict['ERA'], 
                     'yy':yy, 'MM':mm, 'dd':dd}
                    
        raise Exception


    def _calc_ad(self, p_yy, p_jc_from_year):

        ''' 
        西暦変換の計算
        
        Parameters
        ---------
        p_yy : int
            和暦年
        p_jc_from_year : int
            元号開始西暦年
            
        Returns
        ---------
        yyyy : int
            西暦年
        '''

        yyyy = p_yy + p_jc_from_year - 1

        return int(yyyy)


    def _calc_jc(self, p_yyyy, p_ad_from_year):

        ''' 
        和暦変換の計算
        
        Parameters
        ---------
        p_yyyy : int
            西暦年
        p_ad_from_year : int
            元号開始西暦年
            
        Returns
        ---------
        yy : int
            和暦年
        '''

        yy = p_yyyy - (p_ad_from_year - 1)

        return int(yy)


    def is_date(self, p_yyyy, p_mm, p_dd):

        ''' 
        日付存在チェック
        
        Paramters
        ---------
        p_yyyy : string
        p_mm : string
        p_dd : string
        
        Returns 
        ---------
        result : boolean
            True:存在する/False:存在しない
        '''
        
        try:
            date(year=int(p_yyyy), month=int(p_mm), day=int(p_dd))
            return True
            
        except ValueError:
            return False
