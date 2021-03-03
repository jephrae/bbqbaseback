# bbqbaseback

the backend for the bbqbase [bbq base](https://github.com/jephrae/bbqbase "Title") app.

BBQ base is a database of recipes for smoking **meat**. Recipe sites usually _suck_. 
You have to scroll through endless blog content, fight pop up ads, and auto play stuff, and still never find what you need.
BBQ base is different, no ads, no annoying pop ups, just recipes and instructions.
BBQ base is _lightweight_, and **hits** you with only the information you need.
The Data provided by BBQ base is **user created**. There is no end user authentication, by design, instead using a mod system to cull content.

![Screen Shot 2021-03-03 at 17 27 15](https://user-images.githubusercontent.com/55113750/109886485-bd924700-7c45-11eb-8114-65190e5fc845.png)

---

### back-end technologies utilized:
- Python
- Django
- Django Rest Framework
- PostgreSQL
- git 
- heroku

> dependencies for the backend can be installed utilizing _pip install_
---


## User Stories!  :sassy_man: :raising_hand_woman:	:open_book:

- As a user I want to be able to return data from an API call to bbqbaseback.
- As a user I want to be able to POST to the database.
- As an Admin, or mod, I want to be able to edit, and delte entries, as well as creating and reading that the end user can perform. 

---
### unresolved issues and upcoming changes

Maybe, adding a mod route where mods can easily modify db entries.
Eventually enabling file uploads and image hosting? I don't know how viable that is on a free heroku PostgreSQL instance.
