# Tên chương trình
TARGET := piMeter

# Tệp nguồn C++
SRC := main.cpp spiComm.cpp

# Tệp header
HDR :=

# Thư viện
LIBS := -lbcm2835

# Cờ compiler
CFLAGS := -Wall -Wextra -O2

# Quy tắc build chính
build: $(TARGET)

$(TARGET): $(SRC) $(HDR)
	g++ $(CFLAGS) -o $@ $(SRC) $(LIBS)

# Quy tắc clean
clean:
	rm -f $(TARGET) *.o
