- 모든 서비스 시작
docker-compose up

- 특정 서비스 시작
docker-compose up <service_name>

- 서비스 재빌드 및 시작
docker-compose up --build

- 모든 서비스 중지
docker-compose down

- 백그라운드 서비스 중지(관련 네트워크를 제거하지 않음)
docker-compose stop

- 서비스 상태 확인
docker-compose ps

- 서비스 로그 확인
docker-compose logs

- 모든 서비스 재시작
docker-compose restart

- 특정 서비스 재시작
docker-compose restart <service_name>

- 실행 중인 컨테이너에 쉘 접근
docker-compose exec <service_name> /bin/bash

- 특정 서비스 강제 재시작
docker-compose up --force-recreate <service_name>
