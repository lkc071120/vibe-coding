# [import]: 필요한 도구들을 가져옵니다.
import pandas as pd            # 데이터를 표(Table) 형태로 만드는 도구입니다.
from engine import AdvancedDockingSimulator # 아까 만든 '엔진' 설계도를 가져옵니다.

# [if __name__ == "__main__":]: "이 파일을 직접 실행할 때만 아래 코드를 작동시켜라"라는 뜻입니다.
if __name__ == "__main__":
    # ---------------------------------------------------------
    # ?? [사용자 입력창] 여기서 실험 내용을 바꿀 수 있습니다!
    # ---------------------------------------------------------
    TARGET_PDB = "1Z0Q" # 주인공 단백질 ID (알츠하이머)
    CANDIDATES = ["APP", "BACE1", "PSEN1", "APOE", "TREM2", "MAPT", "CLU", "ABCA7"] # 조연 후보들
    # ---------------------------------------------------------

    print("[단계 1] 데이터 생성 및 CSV 저장 시작")

    # 1. 엔진 기계 만들기 및 구조 가져오기
    engine = AdvancedDockingSimulator(TARGET_PDB)
    engine.fetch_structure()

    # 2. 조연들과 결합 에너지 계산하기
    print(f"[*] {len(CANDIDATES)}개의 후보에 대해 계산 중...")
    results = []
    for name in CANDIDATES:
        energy = engine.calculate_energy(name) # 에너지를 계산해서 가져옵니다.
        # [딕셔너리]: {'이름': '값'} 처럼 이름표가 붙은 상자에 데이터를 담는 방식입니다.
        results.append({"Protein_ID": name, "Binding_Energy": energy})
    
    # 3. 데이터 정리 및 정렬
    df = pd.DataFrame(results) # 리스트를 깔끔한 '표(DataFrame)'로 만듭니다.
    
    # [sort_values]: 데이터를 특정 기준(에너지)으로 줄 세웁니다.
    # [reset_index]: 줄을 세우면 번호(인덱스)가 뒤죽박죽되는데, 이를 다시 0, 1, 2... 순으로 만듭니다.
    # [drop=True]: 새로 만든 번호를 기존의 뒤죽박죽된 번호와 겹치지 않게 '버려라'라는 뜻입니다.
    df = df.sort_values(by="Binding_Energy").reset_index(drop=True)
    
    # 4. 순위 매기기
    df['Rank'] = df.index + 1 # 0부터 시작하는 번호에 1을 더해 1등, 2등... 순위를 만듭니다.
    
    # 5. CSV 파일로 저장하기
    # [index=False]: 표의 맨 왼쪽에 붙는 자동 번호(인덱스)는 파일에 저장하지 말라는 뜻입니다.
    df.to_csv("docking_results.csv", index=False) 
    print(f"[+] 완료! 결과가 'docking_results.csv'에 저장되었습니다.")
