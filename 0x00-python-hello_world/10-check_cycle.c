#include "lists.h"

/**
 * check_cycle - A function that checks if a linked list contains a cycle
 *
 * @list: linked list to be checked
 *
 * Return: if 1 the list is a cycle, 0 if it is not
 */
int check_cycle(listint_t *list)
{
	listint_t *normal = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (normal && fast && fast->next)
	{
		normal = normal->next;
		fast = fast->next->next;
		if (normal == fast)
			return (1);
	}

	return (0);
}
