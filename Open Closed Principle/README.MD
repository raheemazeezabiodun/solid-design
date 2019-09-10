#### OPEN CLOSED PRINCIPLE
The open closed principle `(OCP)` states that software entities (classes, modules, functions etc) must be open for extension but closed for modification. [Wikipedia](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

This basically means that when building softwares, a class for example should be easily extended without modifying the class' behaviour for that change

A good example will be how software third party libraries work, you can easily import a method and override it or extend its functionality without modifying the source code. 

>For context - In Django, you can extend the `User`'s model class without directly modifying the Django's `User` class. The software has been clearly written for extension, this is one of the core principles of object oriented programming.

One of the ways to achieve OCP is to rely heavily on Abstraction