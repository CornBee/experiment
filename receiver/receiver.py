import socket
import time

listen_port = 12345

# 로그 파일 경로
log_file_path = '/app/logs/receiver_log.txt'

# 로그 파일에 데이터를 기록하는 함수
def log_data(log_message, mode='a'):  # Default to append; pass 'w' to overwrite
    with open(log_file_path, mode) as file:
        file.write(log_message + '\n')

# 스크립트 시작 시 로그 파일을 비웁니다.
log_data("Starting new receiver log.\n", 'w')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', listen_port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        # 모든 'sender'가 연결되면 5초 기다렸다가 'START' 신호를 보냄
        time.sleep(5)
        conn.sendall('START'.encode('utf-8'))

        while True:
            data = conn.recv(1024)
            receive_time = time.time()

            send_time = data.decode('utf-8')
            delay = receive_time - float(send_time)

            # 로그 파일에 수신 시간 및 지연 시간 기록
            log_data(f"Received at {receive_time}: Sent at {send_time}, Delay: {delay} seconds")
