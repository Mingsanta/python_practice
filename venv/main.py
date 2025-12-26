## UI연습코드
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("PyQt5 테스트")
# window.resize(400, 300)
# window.show()

# sys.exit(app.exec_())


# 시가총액 = 2980000000000
# 현재가 = 50000
# PER = 15.79

# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))


# num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))

# string = "홀짝홀짝홀짝"
# print(string[::2])  #시작인덱스 : 끝인덱스 : 오프셋

# string = "PYTHON"
# print(string[::-1])

# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", '')
# print(phone_number1)

# ticker = "btc_krw"
# ticker1 = ticker.upper()
# print(ticker1)


# date = "2020-05-01"
# print(date.split("-"))


# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("베트맨")
# print(movie_rank)



movie_rank = ["닥터 스트레인지", "스플릿", "럭키", "베트맨"]
del movie_rank[3]
print(movie_rank)
