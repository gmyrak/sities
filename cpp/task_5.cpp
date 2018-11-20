#include <fstream>
using namespace std;

int main()
{
    // Наибольшее четырехзначное
	ifstream inp("input.txt");
	ofstream out("output.txt");

	int n;
	inp >> n;

	int dig[4];
	int i = 0;
	while (n > 0) {
		int k = n % 10;
		dig[i] = k;
		n /= 10;
		i++;
	}

	// Сорртировка массива методом пузырька
	// в порядке убывания
	for (int i = 4; i >= 0; i--) {
		for (int j = 0; j < i-1; j++) {
			if (dig[j] < dig[j + 1]) {
				int tmp = dig[j];
				dig[j] = dig[j + 1];
				dig[j + 1] = tmp;
			}
		}
	}

	for (int i = 0; i < 4; i++) {
		out << dig[i];		
	}

	inp.close();
	out.close();


    return 0;
}