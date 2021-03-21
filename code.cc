#include <stdio.h>

#include <stdio.h>

void examples() {
  // All the following usages of ANSI escape codes have the same effect.
  printf("This is \033[%dm%s\033[0m important.\n", 32, "really");
  printf("This is \033[%sm%s\033[0m important.\n", "32", "really");
  printf("This is \033[%dm%s\033[m important.\n", 32, "really");
  printf("This is \033[%sm%s\033[m important.\n", "32", "really");
}

int main() {
  examples();  
}
