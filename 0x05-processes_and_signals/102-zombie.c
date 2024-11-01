#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);
/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (!pid)
			return (0);

		else
			printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
}

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
