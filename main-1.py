def print_report_card():
    # 1. 정보 및 점수 입력받기
    name = input("이름을 입력하세요: ")
    kor = int(input("국어 점수를 입력하세요: "))
    eng = int(input("영어 점수를 입력하세요: "))
    com = int(input("컴퓨터 점수를 입력하세요: "))

    # 2. 총점 및 평균 계산
    total = kor + eng + com
    avg = total / 3

    # 3. 학점 계산 (평균 점수 기준)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"  # 70점 미만일 경우 F학점 (필요에 따라 D로 변경 가능)

    # 타이틀용 이름 추출 (3글자 이상인 경우 첫 글자(성)를 제외, 아니면 그대로 사용)
    first_name = name[1:] if len(name) >= 3 else name

    # 4. 결과 출력
    print(f"\n********* {first_name}님의 성적표  ***********")
    print(f"이름 : {name}")
    print(f"국어 : {kor}점, 영어 {eng}점, 컴퓨터 : {com}점")
    print(f"총점 : {total}점, 평균 : {int(avg)}점, 학점 : {grade}학점")

# 프로그램 실행
if __name__ == "__main__":
    print_report_card()