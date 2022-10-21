#include "lists.h"

/**
 * is_palindrome - determines if a singly linked list is a palindrome
 * @head: Head node of the list
 *
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
	int list_length = list_len(*head);
	int *val_list = malloc(list_length * sizeof(int));
	int x, y;
	const listint_t *node = *head;

	for (x = 0; x <= (list_length - 1); x++)
	{
		val_list[x] = node->n;
		node = node->next;

	}

	for (x = 0, y = (list_length - 1); x <= (list_length - 1); x++, y--)
	{

		if (x < y)
		{

			if (val_list[x] == val_list[y])
				continue;
			else
				return (0);
		}
		else
			break;
	}

	return (1);
}

/**
 * list_len - Counts the elements of a linked list
 * @h: input head node of list
 *
 * Return: The number of elements in the list
 */
size_t list_len(const listint_t *h)
{
	const listint_t *node = h;
	size_t elenum = 0;

	while (node)
	{
		elenum++;
		node = node->next;
	}
return (elenum);
}
