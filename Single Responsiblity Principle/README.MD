#### SINGLE RESPONSIBILITY PRINCIPLE
The single responsibility principle states that every module, class, or function should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. [Wikipedia](https://en.wikipedia.org/wiki/Single_responsibility_principle)

>**Uncle Bob** emphasizes that a class should have only reason to change.

This basically means that a class, a function should do just one thing and do it very well,
because you can make a class do anything doesn't mean you should make it do many things.
A better way of following the SRP is to have low coupling (the measure of degree of interpedence on between modules) and high cohesion (the degree of how components are related to perform a single task)


The more responsiblity a class has, the more it changes and the more it changes, the likelihood of errors occuring is very high


Let's take a look at some examples
```
#### TOO MUCH RESPONSIBILTY


class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
    def validate_email(self):   # NOTE: DON'T use this validation in production
        return '@' in self.email

    def is_valid_email(self):
        is_valid = False
        if self.validate_email():
            is_valid = True
        return is_valid
```

The above example violates SRP because the Person class shouldn't handle the logic for validating emails. If we finally have a valid regular expression for validating emails, this means we will have to update the `validate_email` in the Person's class.
>Think about it, do we really need to care about the validation logic in the Person's class?

```
###### Better approach

validate.py
def validate_email(email):
    return '@' in email


from validate import validate_email
class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def is_valid_email(self):
        is_valid = False
        if validate_email(self.email):
            is_valid = True
        return is_valid
```
>We don't care about the validation logic, we trust that the `validate_email` will validate the email pretty well. A function must do one thing and do it very well


#### Example 2
```
def create_user(name, age, email):
    # serialize data
    serialized_name = name.strip()
    serialized_age = age.strip()
    serialized_email = email.strip()

    user = Model.save(serialized_name, serialized_age, serialized_email)
    if user:
        email_context = {
            'id': user.id,
            'full_name': user.get_full_name(),
            'password_link': user.generate_password_link
        }
        email_message = render_template_to_string('registration.html', email_context)
        send_email(subject="Hey, Welcome on board", body=email_message, to=user.email)
```

Let's look at what's wrong with the above function

The above `create_user` function does 4 different things
- It serializes the body of the function
- It creates the user
- It creates the email subject
- It sends email to the new user


The question is, does `create_user` depicts the content of the function? NO

A rule of thumb is, if your function name does not reflect the body of the function, it's a bad design

A better name for this class will be `serialize_new_user_and_create_user_and_build_email_template_and_send_email`


Hell No!, that sounds awkward, this brings us into another rule.

*THOU SHALL NOT USE CONJUNCTION WHEN NAMING MODULES, CLASSES, FUNCTIONS*

Keep your functions, classes, modules as simple as possible
