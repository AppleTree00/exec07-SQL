import sqlite3

def view_student_scores():
    # 1. DB 연결
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()

    try:
        # 2. 데이터 조회 SQL 실행 (최신 등록 데이터나 ID 순으로 정렬 가능)
        cursor.execute("SELECT id, name, kor, eng, com, total, avg, grade FROM student_scores ORDER BY id ASC")
        rows = cursor.fetchall()

        # 데이터가 없는 경우 처리
        if not rows:
            print("\n❌ 조회할 성적 데이터가 없습니다. 먼저 데이터를 입력해주세요.")
            return

        # 3. 상단 헤더 출력
        print("\n" + "="*70)
        print(f"{'ID':<4} | {'이름':<9} | {'국어':<5} | {'영어':<5} | {'컴퓨터':<5} | {'총점':<5} | {'평균':<5} | {'학점':<5}")
        print("-" * 70)

        # 4. 각 레코드 반복 출력
        for row in rows:
            # 한글은 영문보다 자리를 많이 차지하므로 이름 출력 시 정렬을 맞추기 위한 처리
            # (한글 이름을 고려하여 일정한 간격 유지)
            student_id, name, kor, eng, com, total, avg, grade = row
            
            # 한글 공백 맞춤을 위해 이름 글자 수에 따라 공백 조절 (3글자 기준 기본 정렬)
            padded_name = name.ljust(6) if len(name) < 3 else name.ljust(5)

            print(f"{student_id:<4} | {padded_name} | {kor:>4}점 | {eng:>4}점 | {com:>4}점 | {total:>4}점 | {avg:>4}점 |  {grade} 학점")
        
        print("="*70)
        print(f"📊 총 {len(rows)}명의 학생 성적이 조회되었습니다.\n")

    except sqlite3.OperationalError as e:
        # 테이블이 존재하지 않을 때 예외 처리
        print(f"\n❌ 오류가 발생했습니다: {e}")
        print("💡 테이블이 아직 생성되지 않았을 수 있습니다. 생성 및 입력 스크립트를 먼저 실행해주세요.")

    finally:
        # 5. 연결 종료
        conn.close()

# 프로그램 실행
if __name__ == "__main__":
    view_student_scores()