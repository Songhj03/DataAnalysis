from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

# 샘플 데이터
data = {
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female'],
    'age': [22, 54, 55, 34, 33, 45, 21, 36],
    'race': ['Caucasian', 'African-American', 'Hispanic', 'Caucasian', 'African-American', 'Caucasian', 'Caucasian', 'African-American'],
    'decile_score': [6, 9, 1, 1, 4, 9, 5, 5],
    'is_recid': [0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# 그래프 생성 함수
def create_plot():
    plt.figure(figsize=(10, 6))
    plt.bar(df['age'], df['decile_score'], color='blue', alpha=0.7, label='Decile Score')
    plt.scatter(df['age'], df['is_recid']*10, color='red', label='Recidivism')
    plt.title('Decile Score and Recidivism by Age')
    plt.xlabel('Age')
    plt.ylabel('Decile Score')
    plt.legend()
    
    # 이미지를 바이트로 변환하여 반환
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_data = base64.b64encode(img_buf.getvalue()).decode('utf-8')
    plt.close()
    
    return img_data

# 루트 경로의 홈페이지
@app.route("/")
def home():
    plot_data = create_plot()
    return render_template("index.html", plot_data=plot_data)

if __name__ == "__main__":
    app.run(debug=True)