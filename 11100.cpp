#include <iostream>
#include <algorithm>
using namespace std;


#define REP(i, b, n) for (int i = b; i < n; i++) // Replica um: for i in range(b, n, 1)
// #define REPI(i, b, n) for (int i = b; i <= n; i++) // Replica um: for i in range(b, n+1, 1)
#define rep(i, n) REP(i, 0, n) // Replica um: for i in range(0, n, 1)
// #define repi(i, n) REPI(i, 0, n) // Replica um: for i in range(b, n, 1)

int main(void) {
    int n;
    int mochila[10002];
    bool taken[10002];
    int tamanho;
    bool primeiro = true;

    while (cin >> n) {
        if (n == 0) break;

        if (primeiro) primeiro = false; else cout << endl;

        rep (i, n) {
            cin >> mochila[i];
            taken[i] = false;
        }

        sort (mochila, mochila + n);

        tamanho = 0;
        int prev = mochila[0];
        int contador = 1;

        REP (i, 1, n) {
            if (mochila[i] == prev) {
                contador++;
            } else {
                if (contador > tamanho) tamanho = contador;
                contador = 1;
                prev = bags[i];
            }
        }

        if (contador > tamanho) tamanho = contador;

        cout << tamanho << endl;
        rep (i, tamanho) {
            for (int j = i; j < n; j += tamanho) {
                if (j > i) cout << " ";
                cout << mochila[j];
            }
            cout << endl;
        }
    }

    return 0;
}