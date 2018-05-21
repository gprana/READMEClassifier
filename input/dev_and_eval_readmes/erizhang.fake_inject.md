#Fake Inject
-----------------------------
[![Build Status](https://travis-ci.org/erizhang/fake_inject.svg?branch=master)](https://travis-ci.org/erizhang/fake_inject)

## A Fake Function Inject Assistant for C
Fake inject is a assistant tool for the fake function replacement during unit test. So that it can be easier to replace the dependancy with test double.

## Hello, fake inject!

Say you have such production code.

```C
//dice.c
#include <stdio.h>
#include "dice.h"
#include <stdlib.h>

int dice_point()
{
	srand(time(NULL));
	int r = ( rand() % 6 ) + 1;
	return r;
}

int isWon()
{
	int points = dice_point();
	if (points > 3){
		return TRUE;
	}
	return FALSE;
}
```
If you would like to test the function `isWon()`, but it depends on the function `dice_point()` which will generate the random number, it's hard to be tested. There is a way to write a fake function of `dice_point()` which is called `dice_point_fake()`
```C

static int closed_share_point(bool write, int value)
{
    static int saved_value;
    if (write) return saved_value;
    return saved_value = value;
}

void set_points(int points)
{
    closed_share_point(false, points);
}

int dice_point_fake()
{
    return closed_share_pont(true, 0);
}
```

So basic replace the `dice_point` with `dice_point_fake` is:
```C
...
#include "fake_inject.h"
...
TEST(DiceTest, GivenDiceWhenPointBiggerThanThreeShallWin)
{
	set_points(3 + 1);
	SET_FAKE_INJECT(dice_point, dice_point_fake);
	CHECK_EQUAL(1, isWon());
	RESET_FAKE_INJECT(dice_point);
}
```

## Cheat Sheet
<table>
    <tr>
        <th>Macro</th>
        <th>Description</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>SET_FAKE_INJECT(function_name, fake_name);</td>
        <td>Use fake function replace original function.</td>
        <td>SET_FAKE_INJECT(dice_point, dice_point_fake);</td>
    </tr>
    <tr>
        <td>RESET_FAKE_INJECT(function_name);</td>
        <td>Reset the fake function to original real function.</td>
        <td>RESET_FAKE_INJECT(dice_point);</td>
    </tr>
</table>
