#include <cmath>
#include <iostream>
#include <ostream>
#include <vector>

int main() {
  int x;
  std::cin >> x;

  int pow = 0;
  x = abs(x);

  auto some = std::vector<int>();
  while (x) {
    some.push_back(x % 10);
    x /= 10;
    pow++;
  }

  if (some.at(0) > 2 && some.size() >= 9) {
    std::cout << 0;
    return 0;
  }

  int i = 0;
  while (some.at(i) == 0) {
    i++;
    pow--;
  }

  int res = 0;
  for (int j = i; j < some.size(); j++) {
    pow--;
    res += some.at(j) * std::pow(10, pow);
  }

  if (x < 0)
    res = -res;

  std::cout << res << std::endl; // ESTE ES EL RESULTADO EL RESULTADO ES LA VARIABLE res

  return 0;
}
