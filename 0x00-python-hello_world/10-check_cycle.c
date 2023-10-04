#include "lists.h"

/**
 * check_cycle - search infinite loop on linkedlists
 * @head_node: linkedlist head
 * Return: 1 if cycle found, 0 otherwise
 */
int check_cycle(listint_t *head_node)
{
	listint_t *f_node = head_node;
	listint_t *b_node = head_node;

	if (!head_node || !head_node->next)
		return (0);

	b_node = b_node->next;
	f_node = f_node->next->next;

	for (; f_node && b_node && f_node->next;)
	{
		if (b_node == f_node)
			return (1);
		b_node = b_node->next;
		f_node = f_node->next->next;
	}
	return (0);
}
