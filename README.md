# django-xapi-client

A set of functions to put, get and process *xAPI statements*.

This is a *Django app* for writing statements to, and reading statements from, an xAPI *Learning Record Store* (LRS) and supporting some processing on them.

This app was initially created by extracting some code from the [CommonSpaces Platform](https://github.com/gtoffoli/commons), and was tested with the [Learning Locker LRS](https://learningpool.com/solutions/learning-locker-community-overview/). Now we have interfaced it also to [TRAX LRS](https://traxlrs.com/).

*django-xapi-client* relies on the *Python* implemetation of the xAPI protocol [TinCanPython](https://github.com/openedx/TinCanPython), developed by Rustici Sofware, as maintained by the [OpenEdx](https://openedx.org/) project. It is still used as an extension of *CommonSpaces* inside a few *Erasmus+* projects. 

This client also implements:
- a UI form for assisting a user in composing xAPI statements manually and sending them to an LRS, as a *self-declaration* of learning-related activities, possibly in *informal learning* contexts;
- a UI form supporting the computation of the URL to be used for getting a *Parameterized Learning Analytics Dashboard* from *Learning Locker*.

As a *Django* app, *django-xapi-client* has to be configured with a set of context variables defined in the *settings* module of the main app, which, in our case. is [commons](https://github.com/gtoffoli/commons) (some of these are *hidden* in a private include file). They include
- HAS_LRS - enabling / disabling the sending of the xAPI statements;
- LRS_VERSION - eg. 1.0.1 or 1.0.3;
- LRS_ENDPOINT - an url defined by the LRS, possibly in relation with a username;
- LRS_USERNAME - mandatory if LRS_AUTH is not provided; 
- LRS_PASSWORD - mandatory if LRS_AUTH is not provided;
- LRS_AUTH - if not provided, it is computed by *TinCanPython*.
