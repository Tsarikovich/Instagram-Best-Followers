# instagram_best_followers

Shows likes stats for your followers/following. Powered by [instagrapi](https://github.com/adw0rd/instagrapi).

<img src="img.png" alt="example" width="550" height="550">

Script has 2 uses
1) It shows dict with likes amount for every your follower
2) It shows dict with likes amount for every your following

You can use this dict to analyze your "dead" followers or following (who doesn't send you likes).

Sorted dict is saved to json. 

### Installing
Python 3.6 
<br>pip install requirements.txt

### Launch script 
First, set your own login and password in credentials.py<br>
I use 2FA in my IG, so I connected pyotp library for generating 2FA codes.
You need your own base32secret, for finding it go to IG -> security -> 2FA -> authentication app -> add (IOS) and just copy it.

However, if you don't wanna do it or you don't use 2FA, you can login simply by your login and password.

If you like it, don't be greedy, star the project :)
