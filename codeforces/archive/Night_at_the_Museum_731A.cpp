// Time: Mar/06/2017 12:03
// Title: A - Night at the Museum
// Submission ID: 25286865
// Language: C++


#include<iostream>
#include<cmath>
#include<string>
using namespace std;
int main()
{
string a;
cin>>a;
int n=min(abs(a[0]-'a'),(26-abs(a[0]-'a')));
for(int i=0;i<a.size()-1;i++)
n+=min(abs(a[i]-a[i+1]),(26-abs(a[i]-a[i+1])));
cout<<n;
}
