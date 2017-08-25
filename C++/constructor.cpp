#include <iostream>
#include <string>

using namespace std;

class AkshatsClass{
public:
	AkshatsClass(){
		cout <<  "basicly __init__():";
	}
	void setname(string x){
		
		name = x;
				
	}

	string getname(){
		return name;
	}
private:
	string name;

};

int main(){
	AkshatsClass a;
	a.setname("sd");
	cout << a.getname();
	return 0;
}

