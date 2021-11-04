"""
Roadrunner
A coyote is chasing a roadrunner and they start out 50 feet apart. If you know how fast they are both traveling, and how far the roadrunner is from safety, determine whether or not the coyote is able to catch the roadrunner. 

Both animals and the roadrunner's safe place are on a straight line.


Task: 
Determine whether or not the roadrunner made it to safety.

Input Format: 
Three integer values, the first value represents the distance the roadrunner is from safety, then the roadrunner's speed (feet/second) and then the coyote's speed (feet/second).

Output Format: 
A string that says 'Meep Meep' if the roadrunner made it, or 'Yum' if the coyote caught up to the roadrunner.

Sample Input: 
10 
5 
20

Sample Output: 
Meep Meep

Explanation: 
The roadrunner is safe because it took them 2 seconds to get to safety while the coyote only got 30 feet closer to the roadrunner in that same amount of time.
"""
#data
s = "Meep Meep" #safe
c = "Yum"              #caught
s_d = 50                # start_distance
d_s = float(input()) #distance_safe #10
r_s = float(input()) #roadrunner_speed #5
c_s = float(input()) #coyote_speed #20

#integration
c_r = (s_d + d_s) / c_s #coyote_run
r_r = d_s / r_s                #roadrunner_run
m_t = c if c_r < r_r else s #made it or not
print(m_t)