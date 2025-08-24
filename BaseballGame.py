# random 모듈을 가져옵니다. 이 모듈은 무작위 수를 생성하는 데 필요한 함수들을 담고 있습니다.
import random

def generate_number():
    """
    0부터 9까지의 서로 다른 숫자 3개를 뽑아 리스트로 반환하는 함수입니다.
    예: 
    """
    # 0부터 9까지의 숫자(range(10)) 중에서
    # 중복 없이 3개의 숫자(3)를 무작위로 뽑습니다.
    # random.sample() 함수는 이 작업을 매우 편리하게 처리해 줍니다.
    numbers = random.sample(range(10), 3)
    return numbers

# 함수가 잘 작동하는지 테스트해 봅시다.
# (실제 게임에서는 이 줄을 지우거나 주석 처리합니다.)
print(generate_number())

def get_player_guess():
    """
    사용자로부터 3자리 숫자를 입력받아 유효성을 검사한 후,
    숫자 리스트로 변환하여 반환하는 함수입니다.
    """
    # 사용자가 유효한 값을 입력할 때까지 무한 반복합니다.
    while True:
        # 사용자에게 안내 메시지를 보여주고 입력을 받습니다.
        guess_str = input("서로 다른 3자리 숫자를 입력하세요: ")

        # 검증 1: 입력된 값의 길이가 3이 아닌 경우
        if len(guess_str)!= 3:
            print("3자리 숫자만 입력해야 합니다.")
            continue # 반복문의 처음으로 돌아갑니다.

        # 검증 2: 입력된 값이 숫자가 아닌 문자를 포함하는 경우
        if not guess_str.isdigit():
            print("숫자만 입력해야 합니다.")
            continue

        # 검증 3: 중복된 숫자가 있는 경우
        # set은 중복을 허용하지 않는 자료구조입니다.
        # "121" -> set("121") -> {"1", "2"} -> 길이가 2이므로 중복이 있음을 알 수 있습니다.
        if len(set(guess_str))!= 3:
            print("서로 다른 숫자를 입력해야 합니다.")
            continue

        # 모든 검증을 통과했다면, 문자열의 각 문자를 정수로 변환하여 리스트로 만듭니다.
        # 예: "123" -> 
        player_guess = [int(digit) for digit in guess_str]
        
        # 유효한 값을 반환하고 반복문을 종료합니다.
        return player_guess
    
def get_score(secret_number, player_guess):
    """
    비밀 숫자와 플레이어의 추측을 비교하여 스트라이크와 볼의 개수를 반환하는 함수입니다.
    반환값은 (스트라이크, 볼) 형태의 튜플입니다.
    """
    strike_count = 0
    ball_count = 0

    # enumerate()를 사용하면 리스트의 인덱스와 값을 동시에 가져올 수 있습니다.
    # 예: player_guess가 이면, (0, 1), (1, 2), (2, 3) 순서로 반복됩니다.
    for i, guess_digit in enumerate(player_guess):
        # 스트라이크 확인: 값과 위치가 모두 같은 경우
        if guess_digit == secret_number[i]:
            strike_count += 1
        # 볼 확인: 값은 존재하지만 위치가 다른 경우
        elif guess_digit in secret_number:
            ball_count += 1
            
    return strike_count, ball_count

# --- 섹션 5: 메인 게임 로직 ---
def play_game():
    """숫자 야구 게임을 실행하는 메인 함수입니다."""
    # 게임 시작 시 비밀 숫자 생성
    secret_number = generate_number()
    attempts = 0 # 시도 횟수 초기화
    max_attempts = 10 # 최대 시도 횟수 설정

    print("숫자 야구 게임을 시작합니다!")
    print(f"컴퓨터가 서로 다른 3자리 숫자를 정했습니다. {max_attempts}번 안에 맞춰보세요.")
    # 개발 중 정답 확인을 위해 임시로 출력 (배포 시 주석 처리)
    # print(f"정답 확인용: {secret_number}")

    # 메인 게임 루프
    while attempts < max_attempts:
        attempts += 1
        print(f"\n--- 시도 {attempts} ---")
        
        # 사용자 추측 받기
        player_guess = get_player_guess()
        
        # 점수 계산
        strikes, balls = get_score(secret_number, player_guess)
        
        # 결과 출력
        print(f"결과: {strikes} 스트라이크, {balls} 볼")
        
        # 승리 조건 확인
        if strikes == 3:
            print(f"\n축하합니다! {attempts}번 만에 숫자를 모두 맞추셨습니다!")
            return # 게임 종료

    # 최대 시도 횟수를 초과한 경우
    print(f"\n아쉽지만 실패했습니다. 정답은 {secret_number}였습니다.")

# 이 스크립트 파일이 직접 실행될 때만 play_game() 함수를 호출합니다.
if __name__ == "__main__":
    play_game()