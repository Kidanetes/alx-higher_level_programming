#include "lists.h"
/**
 * check_cycle - check wheter there is 
 * a loop or not
 * @list: input parameter
 * Return: 1(there is cycle), 0(there is no cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *prev = list, *now = list;

	while (prev && now && now->next)
	{
		prev = prev->next;
		now = now->next->next;
		if (prev == now)
		{
			return (1);
		}
	}
	return (0);
}
