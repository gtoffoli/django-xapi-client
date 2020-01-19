# django-xapi-client
A set of functions to put, get and process xapi statements.

This is a Django app for writing statements to, and reading statements from, an xAPI Learning Record Store (LRS) and supporting some processing on them.

Currently it only includes low-level stuff that has been moved from the CommonS Platform software (gtoffoli/commons repository), whose code relies on the Python xAPI wrapper by Rustici Software: https://github.com/RusticiSoftware/TinCanPython.

In future this client should implement:
- a UI form for assisting a user in composing statements manually and sending them to an LRS: *self-declaration* of learning-related activities, possibly done in informal contexts;
- a UI form for quering the **Learning Locker** LRS through its *Aggregation API*, performing some simple post-processing and visualization of the query results.
