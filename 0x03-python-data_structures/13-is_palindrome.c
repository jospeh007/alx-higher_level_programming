#include "lists.h"

/**
 * is_palindrome - The value palind or not
 * @head: The head of the list
 * Return: 0 if it is not a palindrom
 * 1 if it is a palindrom
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - Check if the function palindrome
 * @head: The head of the list
 * @end: The end of the list
 */
int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
