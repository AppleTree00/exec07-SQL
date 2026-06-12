import sqlite3

def setup_database():
    # 1. DB 연결 (현재 폴더에 grades.db 파일로 생성됨)
    conn = sqlite3.connect('grades.db')
    cursor = conn.cursor()

    # 2. 테이블 생성 스크립트 (SQL)
    # 이름, 국/영/컴 점수와 함께 계산된 총점, 평균, 학점도 저장하도록 구성했습니다.
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        kor INTEGER NOT NULL,
        eng INTEGER NOT NULL,
        com INTEGER NOT NULL,
        total INTEGER NOT NULL,
        avg INTEGER NOT NULL,
        grade TEXT NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("✅ 'student_scores' 테이블이 준비되었습니다.")

    # 3. 10개 레코드 입력 스크립트 (SQL)
    # 이전에 질문하신 '이윤식' 님의 데이터를 포함하여 10개의 샘플을 준비했습니다.
    insert_records_query = """
    INSERT INTO student_scores (name, kor, eng, com, total, avg, grade)
    VALUES 
        ('이윤식', 88, 90, 93, 271, 90, 'A'),
        ('김철수', 75, 80, 85, 240, 80, 'B'),
        ('박영희', 95, 95, 95, 285, 95, 'A'),
        ('정민수', 60, 65, 70, 195, 65, 'F'),
        ('최지훈', 82, 88, 80, 250, 83, 'B'),
        ('강수진', 78, 72, 75, 225, 75, 'C'),
        ('조현우', 92, 85, 90, 267, 89, 'B'),
        ('윤아름', 100, 98, 99, 297, 99, 'A'),
        ('장동건', 65, 70, 75, 210, 70, 'C'),
        ('임유리', 85, 85, 89, 259, 86, 'B');
    """
    
    # 기존에 데이터가 중복해서 들어가는 것을 방지하기 위해 
    # 테이블이 비어있을 때만 10개의 데이터를 넣도록 간단히 체크합니다.
    cursor.execute("SELECT COUNT(*) FROM student_scores")
    count = cursor.fetchone()[0]
    
    if count == 0:
        cursor.execute(insert_records_query)
        print("✅ 10개의 샘플 레코드가 성공적으로 입력되었습니다.")
    else:
        print(f"💡 이미 {count}개의 데이터가 존재하여 샘플 데이터를 추가하지 않았습니다.")

    # 4. 변경사항 저장(commit) 및 연결 종료
    conn.commit()
    conn.close()

# 프로그램 실행
if __name__ == "__main__":
    setup_database()