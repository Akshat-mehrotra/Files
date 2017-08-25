#include <iostream>
#include <string>

using namespace std;
// THE WRONG WAY
class AkshatsClass{
public:
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

