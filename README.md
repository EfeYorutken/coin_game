# what is this?
this is a cli-game where a set of coins are picked to get to the greatest sum of coins

# how to play
- you are given a group of coins, you can only pick a coin from the left or the right
- once you make a desicion your score increase by the amount that the picked coin represents
- the bot picks a coin and increases its score as well
- each time you win a game, a new game starts with one more coin than before
- your objective is to beat the bot as many times as possible

# how it works
each game state can be considered as a node of a binary tree where
- each left child of a given node, p, represents the game state where the left coin is selected from p
- each right child of a given node, p, represents the game state where the right coin is selected from p
```md
            p : [x,y,z]
                /   \
            [y,z]     [x,y]
```
- assuming the player makes the choice that will grant them the highest total score the bot
itterates over both right and left subtrees of the current game state, adding each coin it picks
to its "score" (not the actual score, just a calculation) and substracts the value of the coin
the player might choose, thus evaluating each move it can make. As a result of this evaluation
the bot makes a desicion.
