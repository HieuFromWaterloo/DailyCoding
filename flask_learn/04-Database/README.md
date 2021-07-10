# Database

This allows flask app to interact with existing database
---

- Install sqlalchemy: `pip install flask - sqlalchemy`

- After configuring the db using flask - alchemy in a `.py` file, create the database:

    ```python
    from flaskblog import db, User, Post
    db.create_all()

    # add user >>>>>>>>>>>>>>>
    # OK, for now the pw is plain text but it will need to be hashed
    user_1 = User(username='Hieu', email='hieu@nguyen.ca', password='test123')
    db.session.add(user_1)
    user_2 = User(username='Bo', email='bo@nguyen.ca', password='test123')
    db.session.add(user_2)
    # we need to commit the changes to the db
    db.session.commit()

    # query all users >>>>>>>>>>
    User.query.all()
    # get 1st user
    User.query.first()
    # filter user
    User.query.filter_by(username='Bo').all()

    # accessing user attributes >>>>>
    # get user using id
    user = User.query.get(1)  # id = 1 OR by username;
    user = User.query.filter_by(username='Bo').first()  # first output user without a list
    # get user's posts
    user.posts

    # crreate posts for users
    post1_1 = Post(title='title 1', content='1st post', user_id=user.id)
    post1_2 = Post(title='title 2', content='2nd post', user_id=user.id)
    db.session.add(post1_1)
    db.session.add(post1_2)
    db.session.commit()
    user.posts
    for p in user.posts:
        print(p.title)

    # this is where the `backref` that we set earlier came in handy >>>>>
    post = Post.query.first()
    post.author  # we can access author without having to created it

    # delete everything in the db
    db.drop_all()
    ```
