//
// Created by Yassi on 10/14/2021.
//

#include "unistd.h"

void    print_chars(char *s1, char *s2)
{
    char tab[256] = {0};
    int i;

    i = 0;
    while (s2[i])
    {
        tab[(int)s2[i]] = 1;
        i++;
    }

    i = 0;
    while (s1[i])
    {
        if (tab[(int)s1[i]] == 1)
        {
            write(1, &s1[i], 1);
            tab[(int)s1[i]] = 2;
        }
        i++;
    }
}

int main(int ac, char **av)
{
    if (ac == 3)
    {
        print_chars(av[1] , av[2]);
    }
    write(1, "\n", 1);
    return (0);
}
