#include <fstream>
using namespace std;

int main()
{
    // Целочисленный логарифм
	ifstream inp("input.txt");
	ofstream out("output.txt");
	int n;
	inp >> n;	
	int k  = 0;
	int k2 = 1;
	while (k2 < n) {
		k2 *= 2;
		k++;
	}
	out << k;
	inp.close();
	out.close();

    return 0;
}