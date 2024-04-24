#include <chrono>
#include <cstdint>
#include <iostream>
class DateUtil {
    
public: static uint64_t timeSinceEpochMillisec() {
  using namespace std::chrono;
  return duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
}
}

