#include "lists.h"

/**
 * check_cycle - detects a cycle in singly linked list.
 * @list: the iterated list
 *
 * Return: 0 (No cycle), 1 (There is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
