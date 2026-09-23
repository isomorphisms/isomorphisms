# Forms should work on a $60 phone

A person with a $60 Android phone should be able to fill out a job application, apply for food stamps or health insurance, and finish other necessary paperwork without borrowing a laptop or fighting the website.

This is partly a browser problem and partly a website problem. I do not have a complete design yet. But essential forms should be easy to make correctly, easy to test on low-end phones, and easy to inspect when they fail. The people building them should be able to see what broke instead of making excuses about the user's device.

This is also where the cookie and session work in iBrowser matters. A long form should survive switching apps, renderer death, or the browser process being killed in the background, and come back with the session intact. The browser should preserve as much entered state as it safely can without restoring sensitive fields that should not persist.
