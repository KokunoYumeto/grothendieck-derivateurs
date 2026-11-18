// S2COUNT independent exhaustive enumeration of connected categories <=5 arrows.
// Compile: g++ -O2 -std=c++17 B_small_categories.cpp -o B_small_categories
// No input data from the supplied enumeration is used.
#include <algorithm>
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
struct Census {
 int n,k; vector<int> s,t; vector<vector<int>> m;
 vector<pair<int,int>> holes; vector<tuple<int,int,int>> triples;
 long long count=0,nodes=0; map<string,long long> types;
 bool valid_partial(){
  for(auto [a,b,c]:triples){int ab=m[a][b],bc=m[b][c];
   if(ab>=0 && bc>=0 && m[ab][c]>=0 && m[a][bc]>=0 && m[ab][c]!=m[a][bc])return false;
  } return true;
 }
 bool group(const set<int>& h,int e){
  for(int a:h){bool yes=false;for(int b:h)if(m[a][b]==e&&m[b][a]==e)yes=true;if(!yes)return false;}
  return true;
 }
 string monoid_type(){
  for(int e=0;e<n;e++) if(m[e][e]==e){
   set<int> h;bool left=true,right=true;
   for(int a=0;a<n;a++){h.insert(m[m[e][a]][e]);left&=m[m[e][a]][e]==m[e][a];right&=m[m[e][a]][e]==m[a][e];}
   if((left||right)&&group(h,e)) return "finite-group-reduction-order-"+to_string(h.size());
  }
  assert(n==5); // The sole remaining shape must be the 2-by-2 band plus 1.
  for(int a=1;a<n;a++)for(int b=1;b<n;b++)for(int c=1;c<n;c++){
   assert(m[a][a]==a && m[a][b]>0 && m[m[a][b]][c]==m[a][c]);
  }
  set<vector<int>> rows,cols;
  for(int a=1;a<n;a++){vector<int> rr,cc;for(int b=1;b<n;b++){rr.push_back(m[a][b]);cc.push_back(m[b][a]);}rows.insert(rr);cols.insert(cc);}
  assert(rows.size()==2&&cols.size()==2);return "P2";
 }
 string classify(){
  if(k==1)return monoid_type();
  if(k>=3){
   assert(k==3&&n==5);
   for(int a=k;a<n;a++)assert(s[a]!=t[a]);
   for(int a=k;a<n;a++)for(int b=k;b<n;b++)assert(t[b]!=s[a]);
   return "three-object-V";
  }
  vector<int> cross01,cross10,loops0,loops1;
  for(int a=k;a<n;a++){
   if(s[a]==0&&t[a]==1)cross01.push_back(a);
   if(s[a]==1&&t[a]==0)cross10.push_back(a);
   if(s[a]==0&&t[a]==0)loops0.push_back(a);
   if(s[a]==1&&t[a]==1)loops1.push_back(a);
  }
  if(!cross01.empty()&&!cross10.empty()){
   bool retract=false;for(int f:cross01)for(int g:cross10)if(m[g][f]==0||m[f][g]==1)retract=true;
   assert(retract);return "mutual-arrows-retract";
  }
  auto c=cross01.empty()?cross10:cross01;assert(!c.empty());
  if(c.size()==1)return "unique-cross-arrow-join";
  if(c.size()==3){assert(loops0.empty()&&loops1.empty());return "three-parallel-arrows";}
  assert(c.size()==2);
  vector<int> ell=loops0;ell.insert(ell.end(),loops1.begin(),loops1.end());
  if(ell.empty())return "parallel-pair";
  assert(ell.size()==1);int e=ell[0],v=s[e];
  bool isgroup=m[e][e]==v;assert(isgroup||m[e][e]==e);
  int a=(t[c[0]]==v)?m[e][c[0]]:m[c[0]][e];
  int b=(t[c[1]]==v)?m[e][c[1]]:m[c[1]][e];
  string act;
  if(a==c[0]&&b==c[1])act="trivial";
  else if(a==c[1]&&b==c[0]){assert(isgroup);act="swap";}
  else {assert(a==b&&!isgroup);act="constant";}
  return string("two-cross-")+(isgroup?"C2-":"idempotent-")+act;
 }
 void search(int pos){
  if(pos==(int)holes.size()){assert(valid_partial());count++;types[classify()]++;return;}
  auto [a,b]=holes[pos];
  for(int c=0;c<n;c++)if(s[c]==s[b]&&t[c]==t[a]){
   m[a][b]=c;nodes++;if(valid_partial())search(pos+1);
  }m[a][b]=-1;
 }
 void run_assignment(){
  vector<int> parent(k);iota(parent.begin(),parent.end(),0);
  function<int(int)> find=[&](int a){return parent[a]==a?a:parent[a]=find(parent[a]);};
  for(int a=k;a<n;a++)parent[find(s[a])]=find(t[a]);
  for(int a=1;a<k;a++)if(find(a)!=find(0))return;
  m.assign(n,vector<int>(n,-1));holes.clear();triples.clear();
  for(int a=0;a<n;a++){m[a][s[a]]=a;m[t[a]][a]=a;}
  for(int a=k;a<n;a++)for(int b=k;b<n;b++)if(s[a]==t[b])holes.emplace_back(a,b);
  for(int a=k;a<n;a++)for(int b=k;b<n;b++)for(int c=k;c<n;c++)if(t[c]==s[b]&&t[b]==s[a])triples.emplace_back(a,b,c);
  search(0);
 }
 void assignments(int pos,int low){
  if(pos==n){run_assignment();return;}
  for(int p=low;p<k*k;p++){s[pos]=p/k;t[pos]=p%k;assignments(pos+1,p);}
 }
 void run(){s.resize(n);t.resize(n);for(int i=0;i<k;i++)s[i]=t[i]=i;assignments(k,0);}
};
int main(){
 for(int n=1;n<=5;n++)for(int k=1;k<=n;k++){
  Census c;c.n=n;c.k=k;c.run();
  if(c.count){cout<<"arrows="<<n<<" objects="<<k<<" labelled="<<c.count<<" search_nodes="<<c.nodes<<"\n";
   for(auto [name,num]:c.types)cout<<"  "<<name<<": "<<num<<"\n";}
 }
 cout<<"PASS: every connected category of at most five arrows has an asserted structural type.\n";
}
