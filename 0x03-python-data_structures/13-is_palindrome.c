#include "lists.h"
/**
 * is_palindrome - checks wheteher the list
 * is palindrome or not
 * @head: head of the list
 * Return: 1(palindrome) or
 * 0(not palindrome)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head, *tmp2;
	int i, count = 0;

	if (*head == NULL)
		return (1);
	while((*(*tmp).next).next != NULL)
	{
		tmp = (*tmp).next;
		count++;
	}
	tmp = (*tmp).next;
	count++;
	for (i = 0; i < count; i++, count--)
	{
		if ((**head).n != (*tmp).n)
			return (0);
		*head = (**head).next;
		tmp2 = *head;
		while ((*tmp2).next != tmp)
			tmp2 = (*tmp2).next;
		tmp = tmp2;
	}
	return (1);
}




