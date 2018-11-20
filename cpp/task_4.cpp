#include <fstream>
using namespace std;

int main()
{
    // Количество нечетных элементов
	ifstream inp("input.txt");
	ofstream out("output.txt");	
	int item;
	int k = 0;
	while (! inp.eof()) {
		inp >> item;
		if (item == 0) break;
		if (item % 2 != 0) k++;
		item = 0;
	}
	out << k;
	inp.close();
	out.close();

    return 0;
}