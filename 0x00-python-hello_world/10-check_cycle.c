#include <stdio.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle within.
* @list: singly linked list.
* Return: 0 is there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
