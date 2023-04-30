# Dining Philosophers problem

The dining philosopher's problem is the classical problem of synchronization which says that Five philosophers are sitting around a circular table and their job is to think and eat alternatively. A bowl of noodles is placed at the center of the table along with five chopsticks for each of the philosophers. To eat a philosopher needs both their right and a left chopstick. A philosopher can only eat if both immediate left and right chopsticks of the philosopher is available. In case if both immediate left and right chopsticks of the philosopher are not available then the philosopher puts down their (either left or right) chopstick and starts thinking again.

The above based on the next page: [source here](https://www.javatpoint.com/os-dining-philosophers-problem)

---


How does this work? The solution was based on the following two YouTube videos:

* [Java - Concurrencia - Problema de los filósofos con interbloqueo](https://www.youtube.com/watch?v=nhygnM1lNSM&list=LL&index=36)
* [Java - Concurrencia - Problema de los filósofos con monitores](https://www.youtube.com/watch?v=04FwtQxxAoc&list=LL&index=35&t=33s)

It's Java code implemented in Python. Basically, the use of Monitors was made to solve this problem. There is a class called Chair that is responsible for making 4 philosophers wait seated and one stand. In this way, deadlock is avoided. Why? Because if there are five philosophers sitting on a chair, all of them are going to take the chopstick at the same time, and there will be no free chopstick on the right, so none of the philosophers will be able to eat in their entire lives.

However, if there are only four philosophers at the table sitting in your chair, when they try to take your left chopstick, there will now be a free chopstick. This will allow everyone to eat. But there must be five philosophers at the table and not four. That's why the Chair class works as a monitor. When a philosopher tries to grab a chair and all chairs are taken, the chair class makes that philosopher's thread wait until another philosopher frees a chair and notifies the waiting philosopher of that action.

The purpose of this class is that only the philosophers who have a chair will be the only ones who will be able to take a chopstick at the table. Everyone will think, but everyone will sit down at their time and eat at their time too.