#include <iostream>
#include <map>
#include <string>

using namespace std;

bool isPermutationOfPalindrome(string test){
  // Count the frequency of each char
  int numOfChar = 0;
  map<char, int> charFrequency;
  for(auto c: test){
    if(c == ' '){
      continue;
    }else{
      numOfChar++;
      if(charFrequency.count(c) == 0){
        charFrequency.insert(pair<char, int>(c, 1));
      }else{
        charFrequency[c] += 1;
      }
    }
  }

  // Check the number of odds of frequency
  // If there are more than 1 odds, return false immediately.
  // If there is 1 odd frequency and the number of char is odd, return true.
  // Otherwise, return false.
  int numOfOdd = 0;
  for(map<char, int>::iterator it = charFrequency.begin(); it != charFrequency.end(); it++){
    cout << it->first << ": " << it->second << endl;
    if(it->second % 2 != 0){
      numOfOdd++;
      if(numOfOdd > 1){
        cout << "More than one odds" <<endl;
        return false;
      }
    }
  }

  cout << "numOfOdd: " << numOfOdd << endl;
  cout << test.length() << endl;
  if(numOfOdd == 1 && numOfChar % 2 != 0){
    cout << "1 odd and odd length" << endl;
    return true;
  }else if(numOfOdd == 0){
    cout << "No odd" << endl;
    return true;
  }else{
    return false;
  }
}

int main(){
  string test = "tact coa";
  cout << "It is " << boolalpha << isPermutationOfPalindrome(test) << " that " << test << " is permutation of palindrome" <<endl;
  return 0;
}
