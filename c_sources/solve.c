#include "Land.h"
#define min(a, b) ((a) < (b) ? (a) : (b))
#define MAX 1000000000

rectangle find_rectangle() {
  rectangle answer;
  long long h = MAX, w = MAX;
  long long l = 0, r = MAX;

  while (l < r) {
    long long m = (l + r + 1) / 2;
    long long a = area(0, 0, m, MAX);

    if (a) {
      r = m - 1;
      w = min(a, w);
    }
    else {
      l = m;
    }
  }

  answer.a = l;
  l = 0, r = MAX;

  while (l < r) {
    long long m = (l + r + 1) / 2;
    long long a = area(0, 0, MAX, m);

    if (a) {
      r = m - 1;
      h = min(a, h);
    }
    else {
      l = m;
    }
  }

  answer.b = l;

  answer.c = answer.a + h;
  answer.d = answer.b + w;

  return answer;
}
