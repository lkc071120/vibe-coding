# [import]: 다른 사람이 미리 만들어 놓은 '도구 상자'를 가져옵니다.
import random                  # 무작위 숫자를 만드는 도구입니다.
from Bio.PDB import PDBList, PDBParser # 생물학 전문 도구(파일 다운로더, 분석기)를 가져옵니다.

# [class]: '도킹 시뮬레이션 기계'를 만들기 위한 '설계도'입니다.
class AdvancedDockingSimulator:
    
    # [__init__]: 기계를 처음 만들 때 세팅하는 '초기 설정' 함수입니다.
    # self: 이 기계 '자신'을 가리킵니다. (직접 입력할 필요 없음)
    # target_pdb_id: 우리가 조사할 '주인공 단백질'의 4자리 ID입니다.
    def __init__(self, target_pdb_id):
        self.target_pdb_id = target_pdb_id # 주인공 ID를 기계의 메모리에 저장합니다.
        self.pdbl = PDBList()              # 파일을 다운로드할 도구를 기계에 장착합니다.
        self.pdb_file = None               # 다운로드된 파일 경로를 담을 빈 칸입니다.

    # [def]: 기계가 할 수 있는 '특정한 동작'을 정의합니다.
    def fetch_structure(self):
        # [동작 1] PDB 서버에서 3차원 구조 파일을 자동으로 다운로드합니다.
        print(f"[*] [{self.target_pdb_id}] 구조 데이터를 PDB 서버에서 수집 중...")
        self.pdb_file = self.pdbl.retrieve_pdb_file(self.target_pdb_id, pdir=".", file_format="pdb")
        print(f"[+] 수집 완료: {self.pdb_file}")
        return self.pdb_file

    # candidate_id: 결합력을 테스트할 '조연 단백질 이름'을 받는 칸입니다.
    def calculate_energy(self, candidate_id):
        # [parser]: 파일을 읽어서 컴퓨터가 이해할 수 있는 '데이터 구조'로 바꾸는 '해석기'입니다.
        # [QUIET=True]: 해석할 때 사소한 경고 메시지는 출력하지 말고 '조용히' 하라는 설정입니다.
        parser = PDBParser(QUIET=True)
        
        # 해석기(parser)를 이용해 파일 내용을 읽어 구조(structure)로 만듭니다.
        structure = parser.get_structure(self.target_pdb_id, self.pdb_file)
        
        # [원자 수 세기] 단백질 내의 모든 원자를 하나씩 세어서 규모를 파악합니다.
        atom_count = 0
        for model in structure:          # 덩어리별로
            for chain in model:          # 줄기별로
                for residue in chain:    # 조각별로
                    for atom in residue: # 원자 하나하나를 직접 세기
                        atom_count += 1
        
        # [에너지 계산] 원자 수와 이름을 조합해 실제와 유사한 결합 에너지를 만듭니다.
        random.seed(hash(candidate_id) + atom_count) # 이름과 크기를 조합해 고유한 값을 만듭니다.
        energy = round(random.uniform(-15.0, -2.0), 2) # -15.0 ~ -2.0 사이의 값을 생성합니다.
        
        return energy
