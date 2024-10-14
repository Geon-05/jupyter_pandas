# HTTP상태코드 - 참고사이트
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status
# https://hongong.hanbit.co.kr/http-%EC%83%81%ED%83%9C-%EC%BD%94%EB%93%9C-%ED%91%9C-1xx-5xx-%EC%A0%84%EC%B2%B4-%EC%9A%94%EC%95%BD-%EC%A0%95%EB%A6%AC/
'''
🤔 1XX : Informational(정보 제공)
🤔 2XX : Success(성공)
🤔 3XX : Redirection(리디렉션)
-> 완전한 처리를 위해서 추가 동작이 필요한 경우
-> 주로 서버의 주소 또는 요청한 URI의 웹 문서가 이동되었으니 그 주소로 다시 시도하라는 의미
🤔 4XX : Client Error(클라이언트 에러)
-> 없는 페이지를 요청하는 등 클라이언트의 요청 메시지 내용이 잘못된 경우
🤔 5XX : Server Error(서버 에러)
-> 서버사정으로 메시지 처리에 문제가 발생한 경우
-> 서버의 부하, DB 처리 과정 오류, 서버에서 익셉션이 발생하는 경우
'''