// ----- Y-os -----

@i
M = 0

@SCREEN
D = A

@addres
M = D

(LOOP)
@128
D = A

@i
D = M - D

@LOOP_END
D ; JGE
// ------------


@addres
A = M
M = 1

@32
D = A

@addres
M = D + M


// -----------
@i
M = M + 1

@LOOP
0 ; JMP

(LOOP_END)




// ----- X-os -----

@i1
M = 0

@20480
D = A

@addres1
M = D


(LOOP1)
@8
D = A

@i1
D = M - D

@LOOP_END1
D ; JGE
// ------------


@addres1
A = M
M = -1

@1
D = A

@addres1
M = D + M


// -----------
@i1
M = M + 1

@LOOP1
0 ; JMP

(LOOP_END1)


(END)
@END
0 ; JMP