// LED flashing
#include <at89c51xd2.h>

void my_delay()
{
    TMOD = 0x01;
    TCON = 0x50;
    TL0 = 0x00;
    TH0 = 0x00;
    TR0 = 1;
    while (TF0 == 0);
    TF0 = 0;
    TR0 = 0;
}

void main(void)
{
    P1 = 0x00;
    while (1)
    {
        P1 = 0x00;
        my_delay();
        P1 = 0xFF;
        my_delay();
    }
}

// Hex counter
#include <reg51.h>

void delay()
{
    TMOD = 0x01;
    TCON = 0x50;
    TL0 = 0x00;
    TH0 = 0x00;
    TR0 = 1;
    while (TF0 == 0);
    TF0 = 0;
    TR0 = 0;
}

void main()
{
    int i;
    while (1)
    {
        for (i = 0; i < 16; i++)
        {
            P2 = i;
            delay();
        }
    }
}

// BCD counter
#include <reg51.h>

void delay()
{
    TMOD = 0x01;
    TCON = 0x50;
    TL0 = 0x00;
    TH0 = 0x00;
    TR0 = 1;
    while (TF0 == 0);
    TF0 = 0;
    TR0 = 0;
}

void main()
{
    int i;
    while (1)
    {
        for (i = 0; i < 10; i++)
        {
            P2 = i;
            delay();
        }
    }
}
