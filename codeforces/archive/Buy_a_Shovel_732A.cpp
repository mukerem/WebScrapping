// Time: Mar/08/2017 16:16
// Title: A - Buy a Shovel
// Submission ID: 25341898
// Language: C++


#include<iostream>
using namespace std;
int main()
{
int n,k,c;
cin>>n>>c;
for(int i=1;;i++)
{
if((n*i)%10==c||(n*i)%10==0)
{
cout<<i;
break;
}
}
}
