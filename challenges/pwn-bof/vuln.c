#include <stdio.h>
#include <string.h>

void win() {
    printf("FLAG: CTF{buffer_overflow_controls_execution}\n");
}

void login() {
    char buffer[32];
    printf("Enter username: ");
    gets(buffer);
    printf("Hello, %s\n", buffer);
}

int main() {
    login();
    return 0;
}
