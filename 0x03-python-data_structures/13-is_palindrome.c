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
	int num = 0, i = 0, j = 0;
	int *arr;

	if (*head == NULL || (**head).next == NULL)
		return (1);
	tmp = *head;
	while (*head != NULL)
	{
		num++;
		*head = (**head).next;
	}
	arr = malloc(sizeof(int) * num);
	if (arr == NULL)
		return (0);
	while (i < num)
	{
		arr[i] = (*tmp).n;
		tmp = (*tmp).next;
		i++;
	}
	if (num % 2 == 0)
	{
		i = num / 2;
		j = num / 2 + 1;
	}
	else
	{
		i = (num + 1) / 2 - 1;
		j = (num + 1) / 2 + 1;
	}
	for (; i >= 0 && j < num; i--, j++)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	free(arr);
	return (1);
}
