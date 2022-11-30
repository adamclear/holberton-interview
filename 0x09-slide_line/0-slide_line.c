#include "slide_line.h"
/**
 * slide_line - Slides and merges an array of integers
 * @line: Pointer to the array to be slid and merged
 * @size: Size of the array
 * @direction: Direction to slide, either SLIDE_LEFT or SLIDE_RIGHT
 * Return: 1 on success, otherwise 0
*/
int slide_line(int *line, size_t size, int direction)
{
	if (!line || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT)
	 || size < 1)
	{
		return (0);
	}
	if (direction == SLIDE_LEFT)
		merge_left(line, size);
	else
		merge_right(line, size);
	return (1);
}

/**
 * merge_left - Merges line left
 * @line: Pointer to the array to be merged
 * @size: Size of the array
 * Return: none
*/
void merge_left(int *line, size_t size)
{
	int x = 1, y = 0, z = size - 1;

	while (x <= z)
	{
		if (line[x] == 0)
		{
			x++;
		} else
		{
			if (line[y] == 0)
			{
				line[y] = line[x];
				line[x] = 0;
				x++;
			} else
			{
				if (line[y] == line[x])
				{
					line[y] *= 2;
					line[x] = 0;
					y++;
					x++;
				} else
				{
					y++;
					if (y == x)
						x++;
					else
					{
						line[y] = line[x];
						line[x] = 0;
						x++;
					}
				}
			}
		}
	}
}

/**
 * merge_right - Merges line right
 * @line: Pointer to the array to be merged
 * @size: Size of the array
 * Return: none
*/
void merge_right(int *line, size_t size)
{
	int x = size - 2, y = size - 1;

	while (x >= 0)
	{
		if (line[x] == 0)
		{
			x--;
		} else
		{
			if (line[y] == 0)
			{
				line[y] = line[x];
				line[x] = 0;
				x--;
			} else
			{
				if (line[y] == line[x])
				{
					line[y] *= 2;
					line[x] = 0;
					y--;
					x--;
				} else
				{
					y--;
					if (y == x)
						x--;
					else
					{
						line[y] = line[x];
						line[x] = 0;
						x--;
					}
				}
			}
		}
	}
}
