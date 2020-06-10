#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

typedef struct {
	int sec;
	int min;
	int hr;
}Clock;

void *hours (void *clockObj) {
	
	Clock* newClock = clockObj;
	while(1) {
		sleep(60 * 60);
		newClock -> hr = newClock -> hr + 1;
		newClock -> min = 0;
	}
}

void *minutes (void *clockObj) {
	
	Clock* newClock = clockObj;
	while(1) {
		sleep(60);
		newClock -> min = newClock -> min + 1;
		newClock -> sec = 0;
	}
}

void *seconds (void *clockObj) {
	Clock* newClock = clockObj;
	while(1) {
		sleep(1);
		newClock -> sec = newClock -> sec + 1;
	}
}

void *function(void *clockObj) {
	Clock* newClock = clockObj;
	
	char second[3] = {'\0'};
	char minute[3] = {'\0'};
	char hour[3] = {'\0'};
	
	while(1) {
		if(newClock -> hr < 10)
			sprintf(hour, "0%d", newClock -> hr);
		else
			sprintf(hour, "%d", newClock -> hr);
		if(newClock -> min < 10)
			sprintf(minute, "0%d", newClock -> min);
		else
			sprintf(minute, "%d", newClock -> min);
		if(newClock -> sec < 10)
			sprintf(second, "0%d", newClock -> sec);
		else
			sprintf(second, "%d", newClock -> sec);
		
		printf("%s:%s:%s\r", hour, minute, second);
	}
}

int main() {
		
	Clock *Time = malloc(sizeof(clock));
	Time -> sec = 0;
	Time -> min = 0;
	Time -> hr = 00;	
	
	pthread_t thread1, thread2, thread3, thread4;
	
	pthread_create(&thread1, NULL, &seconds, Time);
	pthread_create(&thread2, NULL, &minutes, Time);
	pthread_create(&thread3, NULL, &hours, Time);
	pthread_create(&thread4, NULL, &function, Time);

	pthread_join(thread1, NULL);
	pthread_join(thread2, NULL);
	pthread_join(thread3, NULL);
	pthread_join(thread4, NULL);

}


