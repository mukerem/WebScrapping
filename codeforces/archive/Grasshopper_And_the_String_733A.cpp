// Time: Mar/08/2017 16:14
// Title: A - Grasshopper And the String
// Submission ID: 25341857
// Language: C++


#include<iostream>
#include<string>
using namespace std;
int main()
{
string n;
int c=0,p=-1;
cin>>n;
for(int i=0;i<n.length();i++)
{
if(n[i]=='A'||n[i]=='E'||n[i]=='O'||n[i]=='I'||n[i]=='U'||n[i]=='Y')
{
c=max(c,i-p);
p=i;
}
}
int k=n.length()-p;
c=max(c,k);
cout<<c;
}
