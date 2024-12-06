# expense_manager_library_sample_usage

이 리포지토리는 expense_manager_library를 설치하고 사용하는 방법을 보여줍니다. expense_manager_library는 개인의 소비 데이터를 분석하고 보고서를 생성하는 파이썬 라이브러리입니다. 

### 라이브러리 및 의존 설치
프로젝트 실행에 필요한 라이브러리와 모듈은 requirements.txt 파일에 정의되어 있습니다.
```bash
pip install -r requirements.txt
```

### 샘플 데이터 사용
examples/sample_data.csv 파일에 샘플 데이터가 있습니다. 

### 사용 예제 실행
examples/폴더에는 라이브러리의 다양한 사용 예제(`example_usage1.py`, `example_usage2.py` 등)가 포함되어 있습니다.
```bash
python examples/example_usage1.py
```
### 결과 확인
결과는 results/ 폴더에 저장됩니다
- **분류된 데이터: classified_data.csv**
- **PDF 보고서: report1.pdf**


