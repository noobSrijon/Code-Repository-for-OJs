#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b;
    cin>>a>>b;
    string A[10]={"one","two","three","four","five","six","seven","eight","nine","Greater than 9"};
    for(int i=a;i<b+1;i++){
        if(i > 9){
            if(i%2==0){
                cout<<"even"<<endl;
            }
            else{
                cout<<"odd\n"<<endl;
            }
        }
        else{
        cout << A[i-1]<<"\n";
        }



    }



    return 0;
}
