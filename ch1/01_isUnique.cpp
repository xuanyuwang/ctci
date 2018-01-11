#include <string>
#include <vector>
#include <iostream>
#include <bitset>
#include <algorithm>

using namespace std;

bool isUnique(const string &str){
    if(str.length() > 128){
        return false;
    }
    vector<bool> char_set(128);
    for (int i = 0; i < str.length(); i++){
        int val = str[i];
        if(char_set[val]){
            return false;
        }
        char_set[val] = true;
    }
    return true;
}

bool isUnique_bit(const string& str){
    bitset<256> bits(0);
    for(int i = 0; i < str.length(); i++){
        int val = str[i];
        if(bits.test(val) > 0){
            return false;
        }
        bits.set(val);
    }
    return true;
}
bool isUnique_noDS(string str){
    sort(str.begin(), str.end());

    bool noRepeat = true;
    for (int i = 0; i < str.size() - 1; i++){
        if (str[i] == str[i+1]){
            noRepeat = false;
            break;
        }
    }
    return noRepeat;
}

int main(){
    vector<string> words = {"abcde", "hello"};
    for(auto word : words){
        cout << word << string(": ") << boolalpha << isUnique(word) << endl;
    }

    cout << endl << "Using bit vector" << endl;
    for(auto word : words){
        cout << word << string(": ") << boolalpha << isUnique_bit(word) << endl;
    }
    
    cout << endl << "Using no Data Structures" << endl;
    for(auto word : words){
        cout << word << string(": ") << boolalpha << isUnique_noDS(word) << endl;
    }

    return 0;
}