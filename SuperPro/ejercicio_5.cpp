#include <cstdlib>
#include <iostream>

int func() {
  int divider = 0;
  int dividend = 0;
  int m = abs(divider);
  int i = 0;

  std::cin >> dividend;
  std::cin >> divider;

  while (1) {
    if (m + abs(divider) == dividend)
      return 0;

    if (m + abs(divider) > dividend)
      break;

    m += abs(divider);
    i++;
  }

  if (int(dividend < 0) + int(divider < 0) == 1)
    return -i;
  return i;
}

int main() { std::cout << func() << "\n"; }
