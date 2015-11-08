#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void check(int t, int* l);

int main(int argc, char* argv[]) {

    int grid[20][20];
    int i = 0;
    int j = 0;
    int index;
    int temp;
    int largest;
    FILE* infile;
    char *buffer = NULL;
    char *digit = NULL;
    size_t read = 0;
    size_t len = 0;

    // A little error handling in the unlikely event of anyone actually trying to use this 
    if (argc < 2) { 
        printf("Format: %s <file.txt>\n", argv[0]);
        exit(1);
    } else {
        infile = fopen(argv[1], "r");
    }

    // Read the file and parse information into a 2D array
    while ((read = getline(&buffer, &len, infile)) != -1) { 
        digit = strtok(buffer, " ");
        while (digit != NULL) {
            index = (int)(strchr(digit, '0') - digit);
            if (index == 0)
                digit = digit + 1;
            grid[i][j] = (int) strtol(digit, (char **)NULL, 10); // found here: http://stackoverflow.com/questions/7021725/converting-string-to-integer-c
            j++;
            digit = strtok(NULL, " ");
        }
        j = 0;
        i++;
    }

    // Search array for maximal product
    for (i = 0; i < 20; i++) {
        for (j = 0; j < 20; j++) {
            if (20 - j > 3) {
                temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3];
                check(temp, &largest);
            }
            if (20 - i > 3) {
                temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j];
                check(temp, &largest);
            }
            if (20 - j > 3 && 20 - i > 3) {
                temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3];
                check(temp, &largest);
            }
            if (j > 3 && 20 - i > 3) {
                temp = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3];
                check(temp, &largest);
            }
        }
    }
    printf("The maximal product is: %d\n", largest);
}

void check(int t, int* l) {
    if (t > *l)
        *l = t;
}
