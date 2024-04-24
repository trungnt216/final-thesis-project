// JsonCpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include "json.hpp"
#include <fstream>

using json = nlohmann::json;

nlohmann::json person = {
    {"name", "Tra cac bu"},
    {"age", 30},
    {"is_student", false}
};

int main()
{
    std::ofstream fileWriter("example.json");
    std::ifstream fileReader("example.json");
    nlohmann::json j;

    std::string json_str = person.dump(); // Serialize to a string
    nlohmann::json deserialized = nlohmann::json::parse(json_str); // Deserialize from a string

    fileWriter << json_str;
    fileWriter.close();

    std::string name = person["name"];
    int age = person["age"];

    std::string line;
    getline(fileReader, line);
    std::cout << line;

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file