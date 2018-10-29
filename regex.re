(?# Pre)
(^ *[A-Z]+ *\n$)



\n\n \n
\n( ?[a-zA-Z\,\.\-])


(?# JOIN DIALOGS)
^([\t ]{2,}[a-zA-Z0-9\,\"\' \.\!\?\&\-]*[a-z0-9\,\' \-])\n\n? ?([a-zA-Z0-9\,\.\-\?\!])
^([\t ]{2,}[a-zA-Z0-9\,\"\' \.\!\?\&\-]*[a-z0-9\,\' ])\n\n? ?([a-zA-Z0-9\,\.\-\?\!])

(?# REMOVE NUMBERS)
^[\t ]*[a-zA-Z]?\-?[0-9]+\.?$


(?# JOIN PARANTESIS)
(^[^\(\n]*\([^\)\n]*)\n *



(\.\.\.) (... )


^( {20}[^ ].*\n)\n( {16}[^ ])

^ {44}([^ ].+)

^ {1,4}([^ ])

^([^ \n])

^ +[0-9]+\.?$

^ +[0-9]+ [0-9]+$

^[0-9]+[a-z] +(.*) +[0-9]+[a-z]$