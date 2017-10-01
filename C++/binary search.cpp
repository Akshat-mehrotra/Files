
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int find = 111;
  int b [10] = {1,3,4,9,13,14,64,77,88,111};
  int endpoint = 9;
  bool found = false;
  int startpoint = 0;
  int half;
  
  if(b[endpoint] == find || b[startpoint] == find){
      cout<<"found it";
      found = true;
      }
  while(found == false){
      
    half = int((endpoint-startpoint)+0.5/2);
    
   if(b[half] == find){
    found = true;
    cout<<"found it at " << half;
   }
    else if(b[half] <find){
        startpoint = half;
        
        }
    else if (b[half] > find){
        endpoint = half;
            }    
        
  }        
  
 
}
