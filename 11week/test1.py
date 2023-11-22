import pandas as pd
import matplotlib.pyplot as plt

# 데이터 프레임 생성
data = {
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female'],
    'age': [22, 54, 55, 34, 33, 45, 21, 36],
    'race': ['Caucasian', 'African-American', 'Hispanic', 'Caucasian', 'African-American', 'Caucasian', 'Caucasian', 'African-American'],
    'decile_score': [6, 9, 1, 1, 4, 9, 5, 5],
    'is_recid': [0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(df['age'], df['decile_score'], color='blue', alpha=0.7, label='Decile Score')
plt.scatter(df['age'], df['is_recid']*10, color='red', label='Recidivism')

plt.title('Decile Score and Recidivism by Age')
plt.xlabel('Age')
plt.ylabel('Decile Score')
plt.legend()
plt.show()