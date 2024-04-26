#include <iostream>
#include <string>
using namespace std;
class PowerMonitor {
	public:
	      	float AIRMS;
	public: 
		float BIRMS;
	public:
	       	float CIRMS;
	public :
		float AVRMS;
	public :
	       	float BVRMS;
	public: 
		float CVRMS;
    // float CVRMS;
	public :
		float AWATT;
	public: 
		float BWATT;
	public : 
		float CWATT;
	public :
	       	float AVAR;
	public:
		 float BVAR;
	public :
	       	float CVAR;
	public:
	       	float AVA;
	public:
	       	float BVA;
	public:
	       	float CVA;
	public:
	       	float AWATTHR_HI;
	public :
		float BWATTHR_HI;
	public :
		float CWATTHR_HI;
	public: uint64_t created_at ;
	public : int index;

    
    
public:
 
    PowerMonitor() {
		
        // Initialize your class if needed
    }
public:
   void logging(){
	    cout << "AIRMS: " << this->AIRMS << endl;
        cout << "BIRMS: " << this->BIRMS << endl;
        cout << "CIRMS: " << this->CIRMS << endl;
        cout << "AVRMS: " << this->AVRMS << endl;
        cout << "BVRMS: " << this->BVRMS << endl;
        cout << "CVRMS: " << this->CVRMS << endl;
        cout << "AWATT: " << this->AWATT << endl;
        cout << "BWATT: " << this->BWATT << endl;
        cout << "CWATT: " << this->CWATT << endl;
        cout << "AVAR: " << this->AVAR << endl;
        cout << "BVAR: " << this->BVAR << endl;
        cout << "CVAR: " << this->CVAR << endl;
        cout << "AVA: " << this->AVA << endl;
        cout << "BVA: " << this-> BVA << endl;
        cout << "CVA: " << this->CVA << endl;
        cout << "AWATTHR_HI: " << this->AWATTHR_HI << endl;
        cout << "BWATTHR_HI: " << this->BWATTHR_HI << endl;
        cout << "CWATTHR_HI: " << this->CWATTHR_HI << endl;
    }
       
};




