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


(end)
@end
0 ; JMP