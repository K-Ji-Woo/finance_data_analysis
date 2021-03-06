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
import numpy as np

xl_path = 'C:\PythonWorkspace\Linked_in_Git\\finance_data_analysis\kodex_leverage.xlsx'

origin_df = pd.read_excel(xl_path)

# 원본 데이터를 복사
df = origin_df.copy()

print(df.shape)
print(df.head(3))
print('\n', df.tail(3))


# 누적 기관순매매량과  누적 외국인순매매량 추가
# 누적 기관순매매량을 DataFrame에 새로운 열로 추가
new_column = range(len(df['종가']))
df['누적_기관순매매량'] = new_column

# 누적 기관순매매량 구하기
df['누적_기관순매매량'][0] = df['기관순매매량'][0]
for i in range(1, len(df.종가)):
    df['누적_기관순매매량'][i] = df['누적_기관순매매량'][i-1] + df['기관순매매량'][i]

# 확인
print(df.shape)
print(df.head(3))
print('\n', df.tail(3))


# 누적 외국인순매매량을 DataFrame에 새로운 열로 추가
new_column = range(len(df['종가']))
df['누적_외국인순매매량'] = new_column

# 누적  외국인순매매량 구하기
df['누적_외국인순매매량'][0] = df['외국인순매매량'][0]
for i in range(1, len(df.종가)):
    df['누적_외국인순매매량'][i] = df['누적_외국인순매매량'][i-1] + df['외국인순매매량'][i]

# 확인
print(df.shape)
print(df.head(3))
print('\n', df.tail(3))


# 종가와 다른 지표들의 상관계수 구하기
print('\n종가와 거래량 상관계수 : ', np.corrcoef(df.종가, df.거래량)[0,1])
print('종가와 기관순매매량 상관계수 : ', np.corrcoef(df.종가, df.기관순매매량)[0,1])
print('종가와 외국인순매매량 상관계수 : ', np.corrcoef(df.종가, df.외국인순매매량)[0,1])
print('종가와 누적_기관순매매량 상관계수 : ', np.corrcoef(df.종가, df.누적_기관순매매량)[0,1])
print('종가와 누적_외국인순매매량 상관계수 : ', np.corrcoef(df.종가, df.누적_외국인순매매량)[0,1])


# 종가와 상관계수가 가장 높은 지표인 누적_기관순매매량을 분석 대상으로 삼음
