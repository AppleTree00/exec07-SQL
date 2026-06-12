import streamlit as st
import sqlite3
import pandas as pd

def view_student_scores_streamlit():
    # 1. 페이지 기본 설정
    st.set_page_config(page_title="학생 성적 조회", page_icon="📊", layout="wide")
    
    st.title("📊 학생 성적표 조회")
    st.markdown("---")

    # 2. '성적조회' 버튼 생성
    # type="primary"를 주면 버튼이 눈에 띄는 색상으로 표시됩니다.
    if st.button("성적조회", type="primary"):
        
        # 버튼이 클릭되었을 때만 DB에 연결하고 데이터를 가져옵니다.
        conn = sqlite3.connect('grades.db')

        try:
            # 3. pandas를 이용해 SQL 데이터를 데이터프레임으로 읽어오기
            query = "SELECT id, name, kor, eng, com, total, avg, grade FROM student_scores ORDER BY id ASC"
            df = pd.read_sql_query(query, conn)

            # 데이터가 없는 경우 처리
            if df.empty:
                st.warning("❌ 조회할 성적 데이터가 없습니다. 먼저 데이터를 입력해주세요.")
            else:
                # 4. 컬럼명(헤더)을 보기 좋은 한글로 변경
                df.columns = ['ID', '이름', '국어(점)', '영어(점)', '컴퓨터(점)', '총점(점)', '평균(점)', '학점']

                # ID 컬럼을 인덱스로 설정하여 기본 인덱스 숨기기
                df.set_index('ID', inplace=True)

                # 5. 화면에 데이터프레임 출력
                st.dataframe(df, use_container_width=True)
                
                # 6. 총 학생 수 출력
                st.success(f"✅ 총 **{len(df)}**명의 학생 성적이 성공적으로 조회되었습니다.")

        except sqlite3.OperationalError as e:
            # 테이블이 존재하지 않을 때 예외 처리
            st.error(f"❌ 오류가 발생했습니다: {e}")
            st.info("💡 테이블이 아직 생성되지 않았을 수 있습니다. 생성 및 입력 스크립트를 먼저 실행해주세요.")

        finally:
            # 7. 연결 종료
            conn.close()

# 프로그램 실행
if __name__ == "__main__":
    view_student_scores_streamlit()