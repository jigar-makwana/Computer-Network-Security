#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

void main(int argc, char **argv){

	int res,j,k=1;
	j = atoi (argv[k]);
	for (k=1;k<=2*j;k++)
	{
	res=fork();
	if(res == 0){
			printf("I am the process %d. My pid is %d\n",k,getpid());
			exit(0);
			}
	else {
		int child_pid = res;
		waitpid(child_pid, NULL,0);
		printf("Father has seen that the child %d exited\n", child_pid);
		}

		}
	}

