#include <fstream>
using namespace std;

int main()
{
    // ���������� �������� ����
	ifstream inp("input.txt");
	ofstream out("output.txt");
	int n;
	inp >> n;
	n = abs(n);
	int k = 0;
	while (n > 0)
	{
		if (n % 2 != 0) k++;
		n /= 10;		
	}
	out << k;

	inp.close();
	out.close();

    return 0;
}