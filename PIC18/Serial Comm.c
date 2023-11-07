/* Baud Rate GENERATION
 * n    => required baudrate
 * BRGH     =   0
 * SPBRG    =   (Fosc / (64 * n)) -1
 * For 9600 baudrate, SPBRG ~=77 */

#include<pic18f4550.h>
void TX_ISR(void);
void RC_ISR(void);
void interrupt chk_isr (void)
{
if (PIR1bits.TXIF==1)
        TX_ISR( );
if (PIR1bits.RCIF==1)
        RC_ISR( );
}
void main(void)
{
    TRISB=0;                 //Set Port B as output
    TRISCbits.TRISC6=0;       // Set TX pin as output
    TRISCbits.TRISC7=1;       //Set Rx pin as input
    TXSTA=0x20;             
    SPBRG=77;                //Baud rate 9600
RCSTAbits.CREN=1;
RCSTAbits.SPEN=1;         //Serial Port Enable
TXSTAbits.TXEN=1;

    PIE1bits.RCIE=1;
    PIE1bits.TXIE=1;
INTCONbits.PEIE=1;         //Enable Peripheral interrupt bit
INTCONbits.GIE=1;          //Enable Global interuupt bit
while(1);
}
void TX_ISR(void)
{
    TXREG='W';
}
void RC_ISR(void)
{
    PORTB=RCREG;
}
