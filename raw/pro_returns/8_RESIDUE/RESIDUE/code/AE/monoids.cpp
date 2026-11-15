// Complete labeled finite-monoid enumeration, identity 0, n <= 5.
// Unknown entries are -1; associativity propagation is sound equality propagation.
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <set>
#include <fstream>
using namespace std;
int n; long long leaves,nodes; set<vector<int>> iso;
bool force(vector<int>& t,int slot,int v,bool&changed){if(t[slot]>=0)return t[slot]==v;t[slot]=v;changed=true;return true;}
bool close_assoc(vector<int>&t){bool changed=true;while(changed){changed=false;for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int c=0;c<n;c++){int ab=t[a*n+b],bc=t[b*n+c];if(ab<0||bc<0)continue;int l=ab*n+c,r=a*n+bc;
 if(t[l]>=0&&!force(t,r,t[l],changed))return false;
 if(t[r]>=0&&!force(t,l,t[r],changed))return false;
 }}return true;}
vector<int> canonical(const vector<int>&t){vector<int>p(n),best;for(int i=0;i<n;i++)p[i]=i;do{vector<int>inv(n),x(n*n);for(int i=0;i<n;i++)inv[p[i]]=i;for(int i=0;i<n;i++)for(int j=0;j<n;j++)x[i*n+j]=inv[t[p[i]*n+p[j]]];if(best.empty()||x<best)best=x;}while(next_permutation(p.begin()+1,p.end()));return best;}
void search(vector<int> t){nodes++;if(!close_assoc(t))return;int slot=-1,best=-1;
 for(int i=1;i<n;i++)for(int j=1;j<n;j++)if(t[i*n+j]<0){int score=0;for(int k=1;k<n;k++){score+=(t[j*n+k]>=0);score+=(t[k*n+i]>=0);}if(i==j)score+=2;if(score>best){best=score;slot=i*n+j;}}
 if(slot<0){leaves++;iso.insert(canonical(t));return;}for(int v=0;v<n;v++){auto s=t;s[slot]=v;search(s);}}
int main(){ofstream out("RESIDUE/code/AE/monoids_tables.json");out<<"[";bool first=true;for(n=1;n<=5;n++){nodes=leaves=0;iso.clear();vector<int>t(n*n,-1);for(int i=0;i<n;i++){t[i]=i;t[i*n]=i;}search(t);cerr<<n<<" nodes "<<nodes<<" labeled "<<leaves<<" isomorphism_classes "<<iso.size()<<"\n";for(auto&t:iso){if(!first)out<<",";first=false;out<<"{\"n\":"<<n<<",\"table\":[";for(int i=0;i<n*n;i++){if(i)out<<",";out<<t[i];}out<<"]}";}}out<<"]\n";}
