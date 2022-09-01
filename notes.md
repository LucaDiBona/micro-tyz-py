atoms
union types
next and prev macros in enumerators

eg foreach i in list {
    if i == next {
        println("same")
    }}

## Blocks

microtyz synatx:

`__block__{}` creates a block - returns value of last expr
`__blockScope__{}` creates a scoped block - creates a new scope and a block within this scope


tyz syntax:

`{}` -> block scope outside loops / if exprs etc.
`{@<blockname>}` -> named scope block
`{@<property>:<blockname>}` -> apply property to block

macro for defining custom blocktypes - eg non scoped block

macros:

macro(100) $left .. $right => range($left,$right)

macro(100) [$*{$vals,}$final] => list($vals + list($final))

macro(50) $decorator:label $target:(<A>)->(<B>-><C>) => $decorator($target)

rough microtyz spec:

call with a universal header file

each line starting with a `#` is processed to create a rules file, all others are ignored

command line args:

header `<filepath>` : loads the header file - every line in header file is treated as a preprocessor directive, no symbol required

directives:

setFlag `<s>` : `<s>` will do the job of `#`

setOpen `<s>` : `#<command><s><...><close>` will run command on whole block

setClose `<s>` : as above

include `<relative filepath>` : include the named file

macro `<prec><open><macro><close><open><replacement><close>` : declare a macro with the relevant precedence

stage `<stage><open><code><close>` : code is run in staged order, with the result of the stage being inserted into the code // look to see how this is usually done

tyz:

setFlag #
setOpen {
setClose }
include .../tyz/lib/std/enter.tyz


