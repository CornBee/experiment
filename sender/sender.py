import socket
import time
import os

# Read the priority from the environment variable
priority = os.getenv('PRIORITY', 'low')

receiver_host = 'receiver'  # 서비스 이름
receiver_port = 12345
number_of_messages = 1000

# 로그 파일 경로 설정
log_file_path = '/app/logs/sender_log.txt'

# 로그 파일에 데이터를 기록하는 함수
def log_data(log_message):
    with open(log_file_path, 'a') as file:
        file.write(log_message + '\n')

# 주기를 결정하는 함수
def get_sleep_duration(priority, iteration):
    if priority == 'high':
        return 1  # important-sender는 항상 1초마다 메시지 전송
    else:
        # less-important-sender는 시간이 지남에 따라 전송 주기를 줄임
        return max(5 - iteration * 0.1, 1)  # 5초에서 시작하여 점점 감소, 최소 1초

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((receiver_host, receiver_port))

    # 'receiver'로부터 시작 신호를 받을 때까지 대기
    start_signal = s.recv(1024)
    if start_signal.decode('utf-8') == 'START':
        for _ in range(number_of_messages):
            iteration = 0

            send_time = time.time()
            message = f"{send_time}"
            s.sendall(message.encode('utf-8'))
            # 로그 파일에 송신 시간 기록
            log_data(f"Sent at {send_time} with priority {priority}")
            # 각 'sender'의 전송 주기 결정
            sleep_duration = get_sleep_duration(priority, iteration)
            time.sleep(sleep_duration)
            iteration += 1