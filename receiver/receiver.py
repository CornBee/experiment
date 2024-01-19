import socket
import time

listen_port = 12345
log_file_path = '/app/logs/receiver_log.txt'

def log_data(log_message, mode='a'):
    with open(log_file_path, mode) as file:
        file.write(log_message + '\n')

log_data("Starting new receiver log.\n", mode='w')

# UDP 소켓 생성
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', listen_port))

while True:
    data, addr = server.recvfrom(1024)  # 데이터와 송신자 주소를 받음
    if not data:
        break
    receive_time = time.time()
    send_time_str, priority = data.decode('utf-8').split(',')
    send_time = float(send_time_str)
    delay = receive_time - send_time
    log_data(f"Received at {receive_time}: Sent at {send_time}, Delay: {delay} seconds, Priority: {priority}\n")
