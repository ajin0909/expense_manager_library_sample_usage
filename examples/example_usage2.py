import os
import sys

# 프로젝트 루트 디렉토리를 sys.path에 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from expense_manager_library.data_cleaner import categorize_transactions
from expense_manager_library.visualizer import load_data
from expense_manager_library.report_generator import generate_report, save_report_to_pdf

#파일 경로 지정, 데이터 가져오기
file_path = "examples/sample_data.csv"
data = file_path

#카테고리 분류
categorized_data = categorize_transactions(data)

#결과를 폴더에 저장
categorized_data = load_data("results/classified_data.csv")

#보고서 생성
report_text = generate_report(
    categorized_data, 
    include_total=True, 
    include_categories=True, 
    include_monthly=True)
print(report_text)

#보고서와 그래프 pdf에 저장
save_report_to_pdf(
    categorized_data,
    report_text, 
    selected_graphs=["pie", "line"], 
    show_report=True,
    pdf_path = "results/report2.pdf")