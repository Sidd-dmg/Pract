#include <reg51.h>

//---------- GENERATE SQUARE WAVE -----------------------------//

void main()
{
    P1 = 0X00; // CONVERT PORT P1 AS OUTPUT

    while(1)
    {
        P1 = 0XFF;
        my_delay();
        P1 = 0X00;
        my_delay();
    }
}

void my_delay()
{
    int i;
    for(i = 0; i < 10000; i++);
}

#include <REG51.h>

//---------- GENERATE TRIANGULAR WAVE -----------------------------//

void delay_ramp(unsigned int time)
{
    unsigned int i, j;
    for(i = time; i > 0; i--)
    {
        for(j = 0; j < 10; j++);
    }
}

void send_dac(unsigned int dat)
{
    P1 = dat;
}

void main(void)
{
    unsigned int a, state = 0xFF;

    while(1)
    {
        // rising ramp edge
        for(a = 0x00; a < 0xFF; a++)
        {
            send_dac(a);
            delay_ramp(1);
        }
        // falling ramp edge
        for(a = 0xFF; a > 0; a--)
        {
            send_dac(a);
            delay_ramp(1);
        }
    }
}
