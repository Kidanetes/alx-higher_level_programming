#include "lists.h"
/**
 * insert_node - insert a number at sorted list
 * @head: input parameter
 * @number: input parameter
 * return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *tmp2, *tmp3;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL);
	if (*head == NULL)
	{
		(*tmp).n = number;
		(*tmp).next = *head;
		*head = tmp;
		return (tmp);
	}
	if ((**head).n > number)
	{
		(*tmp).next = *head;
		(*tmp).n = n;
		*head = tmp;
		return (tmp);
	}
	tmp2 = *head;
	tmp3 = (**head).next;
	while (tmp2 != NULL)
	{
		if (tmp3.n > number)
		{
			(*tmp).n = n;
			(*tmp).next = (*tmp2).next;
			(*tmp2).next = tmp3;
			return (tmp);
		}
		tmp2 = (*tmp2).next;
		tmp3 = (*tmp3).next;
	}
	return (NULL);
}
