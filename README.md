# dotcounter
A python module which will crash the script if any line doesn't contain at least 5 dots

## Usage
Place the ```dotcounter``` directory locally or inside your Python installation's Lib directory.
```
import dotcounter.c.o.u.n.t
```
Somewhere in your script.

## Examples
```
import dotcounter.c.o.u.n.t

x = 5
```
Will cause the error
```
dotcounter.c.o.u.n.t.NotEnoughDotsException: Not enough dots on line: 3
```

Whereas
```
import dotcounter.c.o.u.n.t

x = 1.0 + 1.0 + 1.0 + 1.0 + 1.0
```
Will be fine

Don't try and get around it using comments:
```
import dotcounter.c.o.u.n.t

x = 5 # Ooh....... sneaky comment
```
Will still give the same error.
