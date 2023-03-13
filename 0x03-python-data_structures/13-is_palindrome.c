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
	listint_t *tmp;
	if (*head == NULL || (**head).next == NULL)
		return (1);
	tmp = *head;
	reverse_listint(head);
	   print_listint(*head);
           print_listint(tmp);
	while (*head != NULL)
	{
		if ((**head).n != (*tmp).n)
			return (0);
		*head = (**head).next;
		tmp = (*tmp).next;
	}
	return (1);
}
#include "lists.h"
/**
* reverse_listint - reverse the list
* @head: head node
*
* Return: address of the new head
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp1, *tmp2 = NULL;

	if (*head == NULL)
		return (NULL);
	tmp1 = *head;
	if ((**head).next == NULL)
		return (*head);
	while (*head != NULL)
	{
		tmp1 = (*head)->next;
		(*head)->next = tmp2;
		tmp2 = *head;
		*head = tmp1;
	}
	*head = tmp2;
	return (*head);
}



