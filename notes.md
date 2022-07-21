atoms
union types
next and prev macros in enumerators

eg foreach i in list {
    if i == next {
        println("same")
    }}


macros:

macro(100) $left .. $right => range($left,$right)

macro(100) [$*{$vals,}$final] => list($vals + list($final))

macro(50) $decorator:label $target:(<A>)->(<B>-><C>) => $decorator($target)