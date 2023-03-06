#include "lists.h"
/**
 * check_cycle - check wheter there is 
 * a loop or not
 * @list: input parameter
 * Return: 1(there is cycle), 0(there is no cycle)
 */
int check_cycle(listint_t *list);
{
	listint_t *one = head, *two = head;

	while (one && two && two->next)
	{
		one = one->next;
		two = two->next->next;
		if (one == two)
		{
			one = head;
			while (one != two)
			{
				one = one->next;
				two = two->next;
			}
			return (1);
		}
	}
	return (0);
}
