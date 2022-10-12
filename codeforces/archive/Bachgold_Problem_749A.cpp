// Time: Mar/08/2017 16:47
// Title: A - Bachgold Problem
// Submission ID: 25342576
// Language: C++


#include<iostream>
using namespace std;
int main()
{
int a;
cin>>a;
cout<<a/2<<endl;
for(int i=1;i<a/2;i++)
cout<<2<<"\t";
if(a%2==0)
cout<<2<<"\t";
else
cout<<3<<"\t";
}
