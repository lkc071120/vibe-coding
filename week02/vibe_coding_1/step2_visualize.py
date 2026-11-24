# [import]: 데이터 읽기와 그래프 그리기 도구를 가져옵니다.
import pandas as pd
import matplotlib.pyplot as plt

# [if __name__ == "__main__":]: 이 파일을 직접 실행할 때만 작동합니다.
if __name__ == "__main__":
    print("[단계 2] 저장된 데이터를 읽어 그래프를 그립니다.")

    # 1. CSV 파일 읽기
    try:
        # [pd.read_csv]: 저장된 CSV 파일을 읽어 표(DataFrame)로 만듭니다.
        df = pd.read_csv("docking_results.csv")
        print("[+] 데이터를 성공적으로 불러왔습니다.")
    except FileNotFoundError:
        # [try-except]: 파일이 없을 때 에러를 내며 멈추지 않고, 친절하게 설명하기 위한 장치입니다.
        print("[!] 오류: 'docking_results.csv' 파일이 없습니다. step1을 먼저 실행하세요!")
        exit()

    # 2. 상위 5개만 골라내기
    top_n = 5
    # [head]: 표의 맨 위에서 지정한 숫자(top_n)만큼 데이터만 잘라냅니다.
    df_top = df.head(top_n)

    # 3. 막대 그래프 그리기
    plt.figure(figsize=(10, 6)) # 그래프의 크기(가로, 세로)를 설정합니다.
    
    # [plt.bar]: 막대 그래프를 그리는 명령어입니다.
    # X축: 단백질 이름, Y축: 에너지 값, 색상: 하늘색, 테두리: 남색
    bars = plt.bar(df_top['Protein_ID'], df_top['Binding_Energy'], 
                   color='skyblue', edgecolor='navy')
    
    plt.axhline(0, color='black', linewidth=0.8) # 0점 기준선(가로선)을 그립니다.
    plt.ylabel("Binding Energy (kcal/mol)") # Y축에 이름을 붙입니다.
    plt.title(f"Top {top_n} Binding Affinity") # 그래프 제목을 붙입니다.
    plt.grid(axis='y', linestyle='--', alpha=0.7) # 격자선을 그립니다.

    # 4. 막대 위에 에너지 숫자 써주기
    for bar in bars:
        yval = bar.get_height() # 막대의 높이(에너지 값)를 가져옵니다.
        # [plt.text]: 그래프 위에 글자를 쓰는 명령어입니다.
        plt.text(bar.get_x() + bar.get_width()/2, yval - 0.5, f'{yval}', ha='center', va='bottom')

    plt.tight_layout() # 그래프 요소들이 겹치지 않게 간격을 자동으로 조절합니다.
    
    # 5. 이미지 파일로 저장 및 화면 표시
    plt.savefig("binding_energy_chart.png") # [savefig]: 그래프를 그림 파일로 저장합니다.
    print(f"[+] 완료! 그래프가 'binding_energy_chart.png'로 저장되었습니다.")
    plt.show() # 화면에 그래프를 띄웁니다.
