import streamlit as st
import sqlite3
import pandas as pd

def view_student_scores_streamlit():
    # 1. 페이지 기본 설정
    st.set_page_config(page_title="학생 성적 조회", page_icon="📊", layout="wide")
    
    st.title("📊 학생 성적표 조회")
    st.markdown("---")

    # 2. '성적조회' 버튼 생성
    if st.button("성적조회", type="primary"):
        
        # DB 연결
        conn = sqlite3.connect('grades.db')

        try:
            # 3. 데이터 불러오기
            query = "SELECT id, name, kor, eng, com, total, avg, grade FROM student_scores"
            df = pd.read_sql_query(query, conn)

            if df.empty:
                st.warning("❌ 조회할 성적 데이터가 없습니다. 먼저 데이터를 입력해주세요.")
            else:
                # 4. 컬럼명을 보기 좋은 한글로 변경
                df.columns = ['ID', '이름', '국어(점)', '영어(점)', '컴퓨터(점)', '총점(점)', '평균(점)', '학점']

                # 5. 석차 계산 및 정렬
                df['석차'] = df['총점(점)'].rank(method='min', ascending=False).astype(int)
                df = df.sort_values(by='석차')

                # ID 컬럼을 인덱스로 설정
                df.set_index('ID', inplace=True)

                # 6. 가운데 정렬 스타일 적용
                # 테이블 헤더(th)와 일반 셀(td) 모두 가운데 정렬하도록 설정합니다.
                styled_df = df.style.set_properties(**{'text-align': 'center'}) \
                                    .set_table_styles([dict(selector='th', props=[('text-align', 'center')])])

                # 7. 화면에 스타일이 적용된 데이터프레임 출력
                st.dataframe(styled_df, use_container_width=True)
                
                # 8. 총 학생 수 출력
                st.success(f"✅ 총 **{len(df)}**명의 학생 성적이 석차 순으로 성공적으로 조회되었습니다.")

        except sqlite3.OperationalError as e:
            st.error(f"❌ 오류가 발생했습니다: {e}")
            st.info("💡 테이블이 아직 생성되지 않았을 수 있습니다. 생성 및 입력 스크립트를 먼저 실행해주세요.")

        finally:
            # DB 연결 종료
            conn.close()

# 프로그램 실행
if __name__ == "__main__":
    view_student_scores_streamlit()