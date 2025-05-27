#include <cmath>
#include <iostream>
#include <ostream>
#include <vector>

int main() {
  int x;
  std::cin >> x;
  int pow = 0;
  bool neg = x < 0;

  auto some = std::vector<int>();
  while (x) {
    some.push_back(abs(x) % 10);
    x /= 10;
    pow++;
  }

  auto limit = std::vector<int>({2, 1, 4, 7, 4, 8, 3, 6, 4, 8});
  if (some.size() == limit.size()) {
    for (int i = 0; i < limit.size(); i++) {
      if (some[i] == limit[i])
        continue;
      if (some[i] > limit[i]) {

        std::cout << 0 << "\n";
        return 0;
      }
      break;
    }
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

  if (neg) {
    res = -1 * res;
  }

  std::cout << res << std::endl;

  return 0;
}
