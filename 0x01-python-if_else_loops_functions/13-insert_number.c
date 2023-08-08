#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current; 
	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = (*head);
		(*head) = new;

		return (new);
	}

	current = *head;
	while (current->next && current->next->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);
}

