#include <stdio.h>
#include <string.h>

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
    setup();
    char secret[] = "CTF{format_string_reads_and_writes_memory}";
    char input[64];

    printf("What's your name? ");
    fgets(input, 64, stdin);
    input[strcspn(input, "\n")] = 0;

    printf("Hello, ");
    printf(input);   // <-- THE VULNERABILITY
    printf("\n");

    return 0;
}
