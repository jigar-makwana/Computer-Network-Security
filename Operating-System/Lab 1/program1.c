#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

void main(int argc, char **argv){

	int res;
	
	res=fork();
	if(res == 0){
			char *args[] = {"ls", "-l",NULL};
			printf("I am the child. My pid is %d\n", getpid());
			res = execve("/bin/ls", args,NULL);
			}
	else {
		int child_pid = res;
		printf("I am the father and my pid is %d\n", getpid());
		printf("father is waiting for child to terminate %d\n",child_pid);
		waitpid(child_pid, NULL,0);
		printf("Father has seen that the child  %d exited\n", child_pid);
		}

	
	}

