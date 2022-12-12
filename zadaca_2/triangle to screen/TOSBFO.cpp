#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int crta(int i) {
    int br = 16388 + 480 - 32 + 2048;

    if (i == 0)
        return br + 32;
    else
        return br + (32 * (i+1));

}

int addr(int i) {
    int br = 16388+2048;
    int a = br + 32 * i;
    return a;
}

string brojevi(int i, vector<int> &A) {
    string a = "@" + to_string(A[i]) + "\n";

    return a;
}


int main() {
    vector<int> A = {1, 3};


    for (int i = 1; i < 14; ++i) {
        A.push_back(A[i] * 2 - 1);
    }

    for (auto el: A) {
        cout << el << " ";
    }

    cout << endl << endl;




    // spic ------------

  for (int i = 0; i < 15; ++i) {
      cout << brojevi(i, A) << "D = A" << endl << "@" + to_string(addr(i)) + "\n" << "M = D" << endl << endl;
  }

  cout << endl << endl << endl << endl << endl;



    // crta 1 jedina -------

    for (int i = 0; i <= 112; ++i) {
        cout << "@" + to_string(crta(i)) << endl <<  "M = 1" << endl;
    }


    cout << endl << endl << endl << endl << endl;


    // dijagonala  1 -------------

   for (int i = 0; i < 15; ++i) {
     cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+1+512) << endl << "M = D" << endl << endl;
   }

    cout << endl << endl << endl;

   // dijagonala 2 -------

    for (int i = 0; i < 15; ++i) {
      cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+2+1024) << endl << "M = D" << endl << endl;
    }

    cout << endl << endl << endl;

   // dijagonala 3 ---

     for (int i = 0; i < 15; ++i) {
       cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+3+1024+512) << endl << "M = D" << endl << endl;
     }

    cout << endl << endl << endl;

     // dijag 4 ---

    for (int i = 0; i < 15; ++i) {
      cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+4+1024+1024) << endl << "M = D" << endl << endl;
    }
//

    cout << endl << endl << endl;

    //// dijag 5 ---
//
    for (int i = 0; i < 15; ++i) {
        cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+5+1024+1024+512) << endl << "M = D" << endl << endl;
    }
//

    cout << endl << endl << endl;

    //// dijag 6 ---
//
    for (int i = 0; i < 15; ++i) {
        cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+6+1024+1024+1024) << endl << "M = D" << endl << endl;
    }
//

    cout << endl << endl << endl;


    //// dijag 7 ---
//
    for (int i = 0; i < 15; ++i) {
        cout << "@" << pow(2, i) << endl << "D = A" << endl << "@" + to_string(addr(i)+7+1024+1024+1024+512) << endl << "M = D" << endl << endl;
    }


    return 0;
}
