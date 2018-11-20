#include <fstream>
using namespace std;

int main()
{
    //  оличество нулей в двоичном разложении
	ifstream inp("input.txt");
	ofstream out("output.txt");
	int n;
	inp >> n;	
	n = abs(n);
	int zero = 0;
	while (n > 1) {
		if (n % 2 == 0) zero++;
		n /= 2;					
	}
	out << zero;
	inp.close();
	out.close();

    return 0;
}