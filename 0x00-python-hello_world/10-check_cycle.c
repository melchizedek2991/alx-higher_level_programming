#include "lists.h"

/**
 * check_cycle - This checks if linked list has cycle
 * @list: checking of linked list
 *
 * Return: 1 if list has cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sluggish = list;
	listint_t *hasty = list;

	if (!list)
		return (0);

	while (sluggish && hasty && sluggish->next)
	{
		sluggish = sluggish->next;
		hasty = hasty->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
