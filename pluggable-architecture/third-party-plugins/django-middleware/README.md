# Django Middleware

Creating middleware to add a unique ID to each request.

## Notes

- do not have to override a base class; takes advantage of Duck Typing
  - if class has the functions it needs, the program does not care what it's actual type is
  - if if it quacks like a duck (i.e. has a `.quack()` function), our program treat it like a duck

## Resources

- Django Docs: [Middleware](https://docs.djangoproject.com/en/3.0/topics/http/middleware/)
