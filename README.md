Expense Manager Library Sample Usage
개요
이 리포지토리는 expense_manager_library를 설치하고 사용하는 방법을 보여줍니다. expense_manager_library는 개인의 소비 데이터를 분석하고 보고서를 생성하는 파이썬 라이브러리입니다. 

리포지토리 구조

expense_manager_library_sample_usage/
├── expense_manager_library/    # 라이브러리 소스 코드
│   ├── __init__.py
│   ├── data_cleaner.py
│   ├── report_generator.py
│   └── visualizer.py
├── examples/                   
│   ├── example_usage.py        # 라이브러리 사용 예제
│   └── sample_data.csv         # 샘플 데이터
├── results/                    # 결과 파일 저장 폴더
│   └── (분류된 데이터 및 PDF 파일)
├── README.md                   # 프로젝트 개요 및 사용법
└── requirements.txt            # 의존성 파일

설치 및 사용법
1. 라이브러리 설치
expense_manager_library는 Python 3.7 이상이 필요합니다. 설치는 pip를 통해 수행합니다:

bash
코드 복사
pip install expense_manager_library
2. 샘플 데이터 사용
examples/sample_data.csv 파일에 샘플 데이터가 있습니다. 

3. 사용 예제 실행
examples/example_usage.py는 라이브러리의 주요 기능을 테스트하는 코드입니다. 다음 명령어로 실행할 수 있습니다:

bash
코드 복사
python examples/example_usage1.py
4. 결과 확인
코드 실행 후, 결과는 results/ 폴더에 저장됩니다:

분류된 데이터: classified_data.csv
PDF 보고서: report1.pdf

의존성
프로젝트 실행에 필요한 의존성은 requirements.txt에 정의되어 있습니다. 다음 명령어로 설치할 수 있습니다:

bash
코드 복사
pip install -r requirements.txt
