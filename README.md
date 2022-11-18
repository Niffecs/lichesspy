A client for the lichess.org API
================================================
This is a client library for the Lichess API.
It is designed to be:

* Easy to use

* Customizable when you need it

* Adaptable to API changes

Getting a user's rating:

```python
>>> import lichesspy.api
>>> 
>>> user = lichesspy.api.user('thibault')
>>> print(user['perfs']['blitz']['rating'])
1617
```
Checking who's online and playing:

```python
>>> import lichesspy.api
>>>
>>> users = list(lichesspy.api.users_status(['thibault', 'cyanfish']))
>>> online = [u['id'] for u in users if u['online']]
>>> playing = [u['id'] for u in users if u['playing']]
>>> print(online, playing)
['thibault', 'cyanfish'] ['cyanfish']
```

Saving a PGN of a user's last 200 games:

```python
>>> import lichesspy.api
>>> from lichesspy.format import SINGLE_PGN
>>> 
>>> pgn = lichesspy.api.user_games('thibault', max=200, format=SINGLE_PGN)
>>> with open('last200.pgn', 'w') as f:
>>>    f.write(pgn)
```

Integrating with python-chess:

```python
>>> import lichesspy.api
>>> from lichesspy.format import PYCHESS
>>> 
>>> game = lichesspy.api.game('Qa7FJNk2', format=PYCHESS)
>>> print(game.end().board())
. . k . R b r .
. p p r . N p .
p . . . . . . p
. . . . . . . .
. . . p . . . .
P . . P . . . P
. P P . . P P .
. . K R . . . .
```

Installing
----------
```shell
pip install lichesspy
```
