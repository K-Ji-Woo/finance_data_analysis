"""
# Kodex 레버리지를 이용하여 데이터분석하기(주가와 누적 기관순매매량 중점으로)
* 종가와 상관계수가 큰 지표를 찾고, 그 지표와 종가의 누적 5일 상관계수 지표를 추가
* 기관순매매량과 외국인순매매량 컬럼은 누적량 추가
* Marcov Chain 개념을 이용하여 누적 5일 상관계수를 통해 해당 지표의 변화에 따른 다음날의 추세 변화 예측
"""



"""
## 데이터 로딩 및 전처리
* 필요한 열(누적_기관순매매량, 누적_외국인순매매량) 추가하기
"""
# Python에서 엑셀 파일을 읽으려면 openpyxl 모듈 설치 해야함
import pandas as pd

xl_path = 'C:\PythonWorkspace\Linked_in_Git\\finance_data_analysis\kodex_leverage.xlsx'

origin_df = pd.read_excel(xl_path)

# 원본 데이터를 복사
df = origin_df.copy()

print(df.shape)
print(df.head(3))
print('\n', df.tail(3))


