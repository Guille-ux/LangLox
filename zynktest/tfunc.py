test_cases = [
    'func hola () { print "Hola" ; }',
    'func adios () { print "Adios" ; }',
    'func adios () { print "Adios" ; } call adios ( ) ;',
    'func copy ( x ) { print x ; }',
    'func copy ( x ) { print x ; } call copy ( 1 ) ;',
    'func copy ( x  ) { print x ; } call copy ( "Hola" ) ;'
]