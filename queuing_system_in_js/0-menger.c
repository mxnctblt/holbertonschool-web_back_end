#include "menger.h"

/**
 * menger - Draws a 2D Menger Sponge
 * @level: the level of the Menger Sponge to draw
 * Return: Nothing
 */
void menger(int level)
{
    int size = pow(3, level), i, j, quotient, print_sharp;

    if (level < 0)
        return;

    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size; j++)
        {
            quotient = size / 3;
            print_sharp = 1;
            while (quotient >= 1)
            {
                if ((i / quotient) % 3 == 1 &&
                    (j / quotient) % 3 == 1)
                {
                    printf(" ");
                    print_sharp = 0;
                    break;
                }
                quotient /= 3;
            }
            if (print_sharp == 1)
                printf("#");
        }
        printf("\n");
    }
}
