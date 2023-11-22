import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 엑셀 파일 경로
    excel_path = 'cox-violent-parsed_filt_usable.csv'

    # 엑셀 파일을 읽어 DataFrame으로 로드
    df = pd.read_csv(excel_path)

    # 데이터 분석 및 시각화 (예시: 원 그래프)
    plt.figure(figsize=(8, 8))
    df['Category'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title('Category Distribution')
    plt.savefig('static/pie_chart.png')  # 시각화 결과를 저장

    # 웹페이지에 데이터 전달
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)