// Time: Oct/16/2018 20:06
// Title: A - Packets
// Submission ID: 44411721
// Language: C++


#include<iostream>
#include<cmath>
using namespace std;
int n,ans;
int main(){
    cin>>n;
    ans = int(log2(n)) + 1;
    cout<<ans<<endl;
}

