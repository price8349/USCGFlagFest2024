#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
    FILE *stream;
    FILE *s;
    int size;
    char* in = argv[1];
    char* out = argv[2];
    char *ptr;


    if(argc < 3) return -1;
    char ch;

    // Opening file in reading mode
    stream = fopen(in, "rb");

    if ( !stream )
    {
      fprintf(stderr, "%s: %s: No such file\n", argv[0], argv[1]);
      return 1;
    }
    fseek(stream, 0LL, 2);
    size = ftell(stream);
    fseek(stream, 0LL, 0);
    ptr = malloc(size);
    fread(ptr, 1uLL, size, stream);
    fclose(stream);
    srand(size);
    int *randvals = malloc(size * 3 * sizeof(int));
    for ( int i=0; i < size * 3; i++) {
        randvals[i] = rand();
    }
    printf("created %d rands with seed %d\n", size * 3, size);
    for ( int j = 0; j < size; ++j )
    {
        int v8 = randvals[(size-j)*3 - 2 -1] % (j + 1);
        char v5 = ptr[v8];
        ptr[v8] = ptr[j];
        ptr[j] = v5;
        ptr[j] ^= randvals[(size-j)*3 - 1 -1];
        ptr[v8] ^= randvals[(size-j)*3 -1];
    }
    if ( argc > 2 )
    {
        s = fopen(out, "w");
        fwrite(ptr, 1uLL, size, s);
        free(ptr);
        fclose(s);
        printf("Wrote unscrambled file to \"%s\".\n", argv[2]);
    }
    return 0;
}
