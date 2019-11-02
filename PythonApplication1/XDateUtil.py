# coding: utf-8

from datetime import datetime

class XDateUtil():

    # 和暦辞書
    # {元号コード, 
    #  元号略称, 
    #  元号, 
    #  開始年月日, 
    #  終了年月日,
    #  西暦変換式, 
    #  和暦変換式}
    # --------------------------------------------------------------------------
    # {'ERA_CODE':era_code, 
    #  'ERA_AB':era_ab, 
    #  'ERA':era, 
    #  'FROM':datetime(yyyy,yy,mm),
    #  'TO':datetime(yyyy,yy,mm),
    #  'CALC_AD':'-', 
    #  'CALC_JC':'-'}
    _JC_T_DICT = {'ERA_CODE':0, 
                  'ERA_AB'  :'T', 
                  'ERA'     :'大正', 
                  'FROM':datetime(1912, 7, 30), 
                  'TO'  :datetime(1926, 12, 24), 
                  'CALC_AD':'yy + 1912 - 1', 
                  'CALC_JC':'yyyy - 1912 - 1'}
    _JC_S_DICT = {'ERA_CODE':1, 
                  'ERA_AB'  :'S', 
                  'ERA'     :'昭和', 
                  'FROM':datetime(1926, 12, 25), 
                  'TO'  :datetime(1989, 1, 7), 
                  'CALC_AD':'yy + 1926 - 1', 
                  'CALC_JC':'yyyy - 1926 - 1'}
    _JC_H_DICT = {'ERA_CODE':2, 
                  'ERA_AB'  :'H', 
                  'ERA'     :'平成', 
                  'FROM':datetime(1989, 1, 8), 
                  'TO'  :datetime(2019, 4, 30),
                  'CALC_AD':'yy + 1988 - 1', 
                  'CALC_JC':'yyyy - 1988 - 1'}
    _JC_R_DICT = {'ERA_CODE':3, 
                  'ERA_AB':'R', 
                  'ERA':'令和', 
                  'FROM':datetime(2019, 5, 1), 
                  'TO'  :'-', 
                  'CALC_AD':'-', 
                  'CALC_JC':'-'}
    
    # 和暦リスト
    _JC_DICT = [_JC_T_DICT, _JC_S_DICT, _JC_H_DICT, _JC_R_DICT]
    
    
    def __init__(self):
        ''' コンストラクタ '''


    def toAd(self, p_jc, p_yy, p_mm, p_dd):
    
        ''' 和暦から西暦に変換する。
            変換できない場合は例外を投げる。
        
        Parameters
        ----------
        p_jc : string
            元号（大正、昭和、平成、令和）
        p_yy : string
            年（yy）
        p_mm : string
            月（mm）
        p_dd : string
            日（dd）
            
        Returns
        ----------
        {'yyyy':yyyy, 'MM':mm, 'dd':dd} : dect
            西暦辞書
        '''
        
        yy = p_yy
        for _jc in _JC_DICT:
            if p_jc == _jc['ERA']:
                # 西暦変換
                if '-' == _jc['CALC_AD']:
                    # 現在の西暦年
                    today = datetime.datetime.today()
                    yyyy = today.year
                    
                else:
                    yyyy = eval(_jc['CALC_AD'])
                
                # 妥当性チェック
                if is_date(yyyy, p_mm, p_dd):
                    return {'yyyy':yyyy, 'MM':p_mm, 'dd':p_dd}
                    
        raise Exception
        
        
    def is_date(self, p_yyyy, p_mm, p_dd):
        ''' 日付存在チェック
        
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
            datetime.date(year=p_yyyy, month=p_mm,day=p_dd)
            return True
            
        except ValueError:
            return False
