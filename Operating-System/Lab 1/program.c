#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

void main(int argc, char **argv){

	int res,k;
	for (k=1;k<argc;k++)
	{
	res=fork();
	if(res == 0){
			printf("I am the child. My pid is %d\n",getpid());
			exit();
			}
	else {
		int child_pid = res;
		waitpid(child_pid, NULL,0);
		printf("Father has seen that the child %d exited\n", child_pid);
		}

		}
	}

