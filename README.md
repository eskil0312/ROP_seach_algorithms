# ROP search algorithms
Different search algorithms for ROP optimization.

To demonstrate and test different search methods a random generated surface plot is made. The random surface plot is not important in it self, but it demonstrates how a ROP function might look like with RPM and WOB as parameters.

![image](https://user-images.githubusercontent.com/25080147/38618002-b2cb1f16-3d98-11e8-91cf-68c0ab75e91e.png)

---

## Brute force seach algorithm

![image](https://user-images.githubusercontent.com/25080147/38618227-465585b4-3d99-11e8-8418-e428c9f9a634.png)

The algorithm gives the following output.

 >Best ROP = 84.9819313312 with RPM = 15.0 and WOB = 10.5
 >Number of iterations: 14280
 
 Plotting only when the algorithm find a new highest ROP. Plotting all seaches will fill the entire plot.

## Column seach algorithm
 All ROP plot          |  Best ROP plot 
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/25080147/38618452-03f8b10e-3d9a-11e8-9929-7942fb0556ad.png)  |  ![image](https://user-images.githubusercontent.com/25080147/38618494-200e597a-3d9a-11e8-89ba-338e1571c27f.png)

The algorithm gives the following output.

>Best ROP = 84.9819313312 with RPM = 15.0 and WOB = 10.5
>Number of iterations: 2640

Notice how the number of iterations reduce drastically from the brute force algorithm and resulting in the same ROP
## Column-row seach algorithm

The algorithm gives the following output.

>Best ROP = 84.9819313312 with RPM = 15.0 and WOB = 10.5
>Number of iterations: 480

All ROP plot          |  Best ROP plot 
:-------------------------:|:-------------------------:
![image](https://user-images.githubusercontent.com/25080147/38618803-ef5be3e6-3d9a-11e8-812a-6a66d304adf0.png)  |  ![image](https://user-images.githubusercontent.com/25080147/38618880-1f70f9a4-3d9b-11e8-9eeb-2a5d259dce4b.png)

The best seach algorithm with the least amount of iterations.
