#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

bool isPermutation_sort(string str1, string str2){
  if (str1.length() != str2.length()){
    return false;
  }

  sort(str1.begin(), str1.end());
  sort(str2.begin(), str2.end());

  for(int i = 0; i < str1.length(); i++){
    if(str1[i] != str2[i]){
      return false;
    }
  }

  return true;
}

bool isPermutation_count(const string& str1, const string& str2){
  if(str1.length() != str2.length()){
    return false;
  }
  int count[256] = {0};
  for(int i = 0; i < str1.length(); i++){
    int val = str1[i];
    count[val]++;
    val = str2[i];
    count[val]--;
  }
  for(int i = 0; i < 256; i++){
    if(count[i] != 0){
      return false;
    }
  }
  return true;
}


int main(){
  string str1 = "testcase";
  string str2 = "casetest";
  cout << "Method 1: Using sort" << endl;
  if(isPermutation_sort(str1, str2)){
    cout << str1 << " with " << str2 << " are permutation of each other" << endl;
  }else{
    cout << str1 << " with " << str2 << " are not permutation of each other" << endl;
  }

  cout << "Method 2: Using count" << endl;
  if(isPermutation_count(str1, str2)){
    cout << str1 << " with " << str2 << " are permutation of each other" << endl;
  }else{
    cout << str1 << " with " << str2 << " are not permutation of each other" << endl;
  }
}
