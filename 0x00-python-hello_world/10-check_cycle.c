#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fNode = list;
	listint_t *sNode = list;

	while(fNode != NULL && sNode != NULL)
	{
		sNode = sNode->next;
		if (fNode->next == NULL)
			return(0);
		fNode = fNode->next;
		fNode = fNode->next;

		if (fNode == sNode)
			return(1);
	}
	return(0);
}
