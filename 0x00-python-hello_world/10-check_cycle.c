#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle in it
 * @list: list ptr
 * Return: 0 for  no cycle,
 * 1for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *secondptr;
	listint_t *last;

	secondptr = list;
	last = list;
	while (list && secondptr && secondptr->next)
	{
		list = list->next;
		secondptr = secondptr->next->next;

		if (list == secondptr)
		{
			list = last;
			last =  secondptr;
			while (1)
			{
				secondptr = last;
				while (secondptr->next != list && secondptr->next != last)
				{
					secondptr = secondptr->next;
				}
				if (secondptr->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
