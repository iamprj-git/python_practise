#include <stdio.h>
#include <string.h>

void longest_substring(char str[]) {
    int end = strlen(str);
    int start = 0;
    int longest_length = 0;
    int longest_start = 0;
    
    for (int i = 0; i < end; i++) {
        for (int j = start; j < i; j++) {
            if (str[i] == str[j]) {
                start = j + 1;
                break;
            }
        }
        int sub_length = i - start + 1;
        if (sub_length > longest_length) {
            longest_length = sub_length;
            longest_start = start;
        }
    }
    
    // Print the longest substring
    printf("Longest substring: ");
    for (int k = longest_start; k < longest_start + longest_length; k++) {
        printf("%c", str[k]);
    }
    printf("\n");
}

int main() {
    char str[] = "anishasdnsjddsksednsdwefg";
    longest_substring(str);
    return 0;
}

