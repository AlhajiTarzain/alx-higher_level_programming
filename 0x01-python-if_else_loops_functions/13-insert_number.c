#include <stdlib.h>
#include "lists.h"

/**
 * *insert_node - puts number in clone
 * @head: ptrto address of head of list
 * @number: new node int
 * Return: address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nextnode, *clone;

	nextnode = malloc(sizeof(listint_t));
	if (nextnode == NULL)
		return (NULL);
	if (*head == NULL)
	{
		nextnode->n = number;
		nextnode->next = *head;
		*head = nextnode;
		return (nextnode);
	}
	else if (number <= (*head)->n)
	{
		nextnode->n = number;
		nextnode->next = *head;
		*head = nextnode;
		return (nextnode);
	}
	else
	{
		clone = *head;
		while (clone->next != NULL && number > clone->next->n)
		{
			clone = clone->next;
		}
		nextnode->n = number;
		nextnode->next = clone->next;
		clone->next = nextnode;
		return (nextnode);
	}
	return (NULL);
}
