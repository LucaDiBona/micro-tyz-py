# Expressions

Tyz is made up of expressions, that each return a value and can be nested inside oneanother

# Variables

`var x = 2` creates a variable x with value 2
`let y = 3` creates a const y with value 3
`var x: int = 2` creates a variable x with specific type int and value 2
`y := x` binds y to x (useful if x is, for example, a specific item in a list)
`y := (x)` binds y to the value of x, equivalent to `let y = x`
`y = x` reasigns y to the current value of x
`y <- x` shallow copies x into y
` y <<- x` deep copies x into y

## Differences

If we have `var x = [(0,1),True,[["abc"],["def"]],&foo,Bar(0)]`, where `foo` is a variable equal to `3` and `Bar` is a class with a `value` value and an `__increment__` method that increments this:

Binding:

```
y := x
y[1] = False
printLn(x[1]) //prints False
```

Reassignment

```
y = x
y[1] = False
y[3] ++
y[4] ++
printLn(x[1]) //prints True
printLn(x[3]) //prints 4
printLn(x[4].value) //prints 1
```

Copying

```
y <- x
y[1] = False
y[3] ++
y[4] ++
printLn(x[1]) //prints True
printLn(x[3]) //prints 4
printLn(x[4].value) //prints 0
```

Deep Copying

```
y <<- x
y[1] = False
y[3] ++
y[4] ++
printLn(x[1]) //prints True
printLn(x[3]) //prints 3
printLn(x[4].value) //prints 0
```
