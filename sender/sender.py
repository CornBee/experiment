import socket
import time
import os

send_interval = float(os.getenv('SEND_INTERVAL', '1'))
priority = os.getenv('PRIORITY', 'low')

receiver_host = 'receiver'
receiver_port = 12345
number_of_messages = 1000

log_file_path = '/app/logs/sender_log.txt'

def log_data(log_message, mode='a'):
    with open(log_file_path, mode) as file:
        file.write(log_message + '\n')

log_data("Sender script started.\n", mode='w')

# UDP 소켓 생성
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(number_of_messages):
    send_time = time.time()
    message = f"{send_time},{priority}"
    client.sendto(message.encode('utf-8'), (receiver_host, receiver_port))
    log_data(f"Sent at {send_time} with priority {priority}")
    time.sleep(send_interval)
