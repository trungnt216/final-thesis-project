#include "spiComm.h"
#include "influxdb.hpp"
#include <unistd.h>
#include <stdint.h>
#include <iostream>
#include <fstream> // For file operations
#include <string>
#include "storage.cpp"
#include "json.hpp" // JSON library, e.g., nlohmann/json

using namespace std;
using json = nlohmann::json; // JSON namespace alias

int main() {
    spiComm commObj;

    // influxdb_cpp::server_info si("IP", 8086, "DB", "user", "password");
    std::vector<PowerMonitor> myObjects;

    while(1) {
        PowerMonitor monitor ;
        monitor.AIRMS =  commObj.readCurrent(R_AIRMS_REGISTER);
        monitor.BIRMS =  commObj.readCurrent(R_BIRMS_REGISTER);
        monitor.CIRMS =  commObj.readCurrent(R_CIRMS_REGISTER);
        monitor.AVRMS =  commObj.readVoltage(R_AVRMS_REGISTER);
        monitor.BVRMS =  commObj.readVoltage(R_BVRMS_REGISTER);
        monitor.CVRMS =  commObj.readVoltage(R_CVRMS_REGISTER);
        monitor.AWATT =  commObj.readPower(R_AWATT_REGISTER);
        monitor.BWATT =  commObj.readPower(R_BWATT_REGISTER);
        monitor.CWATT =  commObj.readPower(R_CWATT_REGISTER);  
        monitor.AVAR  =  commObj.readPower(R_AVAR_REGISTER);
        monitor.BVAR  =  commObj.readPower(R_BVAR_REGISTER);
        monitor.CVAR  =  commObj.readPower(R_CVAR_REGISTER); 
        monitor.AVA   =  commObj.readPower(R_AVA_REGISTER);
        monitor.BVA   =  commObj.readPower(R_BVA_REGISTER);
        monitor.CVA   =  commObj.readPower(R_CVA_REGISTER);
        monitor.AWATTHR_HI = commObj.readEnergy(R_AWATTHR_HI_REGISTER);
        monitor.BWATTHR_HI = commObj.readEnergy(R_BWATTHR_HI_REGISTER);
        monitor.CWATTHR_HI = commObj.readEnergy(R_CWATTHR_HI_REGISTER);
        
        myObjects.push_back(monitor);

        // Sleep for 5 seconds
        sleep(5);

        // Convert vector to JSON
        json jsonArray;
        for(const auto& obj : myObjects) {
            json jsonObj = {
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
                {"CWATTHR_HI", obj.CWATTHR_HI}
            };
            jsonArray.push_back(jsonObj);
        }

        // Write JSON to file
        std::ofstream outputFile("output.json");
        outputFile << jsonArray.dump(4); // dump(4) for pretty printing with indentation
        outputFile.close();
        myObject.clear();

    }
}
