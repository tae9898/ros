# ros
- 인용 : https://github.com/rookiecj/ros_facedetect
  
- 변경내용 : 얼굴위치에 따라 퍼블리셔 >> 리스너 >> 아두이노 통신을 통해 led 변화

- python,ros,opencv

토픽으로 제작하였습니다.

1. 퍼블리셔에서 opencv 이용 haarcascade 필터로 사람정면얼굴 감지
2. 사람 좌표 위치 출력
3. 좌표중 x좌표 슬라이싱하여 pub
4. sub(파일명은 listener)에서 정보 전달받은 string시리얼 통신 
5. string을 int형으로 변환, 값에 따라 led변환


![GifMaker_20240220152902622](https://github.com/tae9898/ros/assets/113410967/a4e3a8d1-f7c0-460c-b9d8-2f291e163ebb)
