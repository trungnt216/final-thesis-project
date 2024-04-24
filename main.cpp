#include <stdint.h>
#include <unistd.h>

#include <fstream>  // For file operations
#include <fstream>
#include <iostream>
#include <string>

#include "influxdb.hpp"
#include "json.hpp"  // JSON library, e.g., nlohmann/json
#include "spiComm.h"
#include "storage.cpp"
#include "utils/date.cpp"

using json = nlohmann::json;
using namespace std;

int main() {
  spiComm commObj;
  std::vector<PowerMonitor> myObjects;
  int count = 0;
  string prefix = "./data/metter_output_";
  string extension = ".json";
  string metterFileName =
      prefix + to_string(DateUtil::getTimeSinceEpochMillisec()) + extension;
  json jsonArray = json::array();
  json jsonObject;
  cout << "Begin program";
  while (1) {
    PowerMonitor monitor;
    monitor.index = count++;
    monitor.AIRMS = commObj.readCurrent(R_AIRMS_REGISTER);
    monitor.BIRMS = commObj.readCurrent(R_BIRMS_REGISTER);
    monitor.CIRMS = commObj.readCurrent(R_CIRMS_REGISTER);
    monitor.AVRMS = commObj.readVoltage(R_AVRMS_REGISTER);
    monitor.BVRMS = commObj.readVoltage(R_BVRMS_REGISTER);
    monitor.CVRMS = commObj.readVoltage(R_CVRMS_REGISTER);
    monitor.AWATT = commObj.readPower(R_AWATT_REGISTER);
    monitor.BWATT = commObj.readPower(R_BWATT_REGISTER);
    monitor.CWATT = commObj.readPower(R_CWATT_REGISTER);
    monitor.AVAR = commObj.readPower(R_AVAR_REGISTER);
    monitor.BVAR = commObj.readPower(R_BVAR_REGISTER);
    monitor.CVAR = commObj.readPower(R_CVAR_REGISTER);
    monitor.AVA = commObj.readPower(R_AVA_REGISTER);
    monitor.BVA = commObj.readPower(R_BVA_REGISTER);
    monitor.CVA = commObj.readPower(R_CVA_REGISTER);
    monitor.AWATTHR_HI = commObj.readEnergy(R_AWATTHR_HI_REGISTER);
    monitor.BWATTHR_HI = commObj.readEnergy(R_BWATTHR_HI_REGISTER);
    monitor.CWATTHR_HI = commObj.readEnergy(R_CWATTHR_HI_REGISTER);
    monitor.created_at = DateUtil::getTimeSinceEpochMillisec();

    myObjects.push_back(monitor);
    monitor.logging();

    // Sleep for 5 seconds
    sleep(5);

    // Convert vector to JSON

    for (const auto& obj : myObjects) {
      json jsonObj = {{"index", obj.index},
                      {"AIRMS", obj.AIRMS},
                      {"BIRMS", obj.BIRMS},
                      {"CIRMS", obj.CIRMS},
                      {"AVRMS", obj.AVRMS},
                      {"BVRMS", obj.BVRMS},
                      {"CVRMS", obj.CVRMS},
                      {"AWATT", obj.AWATT},
                      {"BWATT", obj.BWATT},
                      {"CWATT", obj.CWATT},
                      {"AVAR", obj.AVAR},
                      {"BVAR", obj.BVAR},
                      {"CVAR", obj.CVAR},
                      {"AVA", obj.AVA},
                      {"BVA", obj.BVA},
                      {"CVA", obj.CVA},
                      {"AWATTHR_HI", obj.AWATTHR_HI},
                      {"BWATTHR_HI", obj.BWATTHR_HI},
                      {"CWATTHR_HI", obj.CWATTHR_HI},
                      {"created_at", obj.created_at}};
      jsonArray.push_back(jsonObj);
    }

    jsonObject["data"] = jsonArray;

    // Write JSON to file
    std::ofstream outputFile(metterFileName);
    // outputFile << jsonObject.dump(4); // dump(4) for pretty printing with
    // indentation
    if (!outputFile.is_open()) {
      std::cout << "\n Failed to open output file";
    } else {
      outputFile << jsonObject.dump(4);
      myObjects.clear();
      outputFile.close();
    }
    if (jsonArray["data"].size() > 20) {
      // tạo file mới mới.
      metterFileName =
          prefix + to_string(DateUtil::getTimeSinceEpochMillisec()) + extension;
      count = 0;
      jsonArray.clear();
    }
   
  }
}