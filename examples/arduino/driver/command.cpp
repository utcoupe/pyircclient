#include "command.h"
#include "led.h"



/**
 * Analyse du message et lancement de la fonction associée à la commande
 * @param id id du message
 * @param id_cmd id de la commande
 * @param args tableau d'arguments
 * @param size nombre d'arguments
 */
void cmd(int id, int id_cmd, int *args, int size){
    switch(id_cmd)
    {
		case Q_ID:
		{
			sendMessage(id, "samplebot");
			break;
		}
		case Q_PING:
		{
			sendMessage(id, "pong");
			break;
		}
		case Q_ALLUME:
		{
			if (size < 1)
				sendMessage(id, E_INVALID_PARAMETERS_NUMBERS);
			else
			{
				allumeLed(args[0]);
			}
			break;
		}
		case Q_ETEINDRE:
		{
			if (size < 1)
				sendMessage(id, E_INVALID_PARAMETERS_NUMBERS);
			else
			{
				eteindreLed(args[0]);
			}
			break;
		}
		default:
		{
			sendMessage(id,-1);
			break;
		}
    }
}
