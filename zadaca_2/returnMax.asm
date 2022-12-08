// ---- R0 dio ----

@R0		// sett R0 to R5
D = M
@R5
M = D

// ---- R1 dio ----


@R5
D = M // setao si D na vrijednost iz R5


@JMPHere1
0 ; JMP


(SWAP1)
// kod za swap

@R5		// D je setan na vrijednost iz R5
D = M
@R0		//temp je setan na vrijednost iz R5
M = D

@R1		// R5 sett to R1
D = M
@R5
M = D

@R0		// R1 sett to temp
D = M
@R1
M = D


(JMPHere1)


@R1
D = D - M  //oduzimanje

@SWAP1
D ; JLT


// R5 = 10 max, R1 = 2 =>  8 < 0


// ---- R2 dio ----


@R5
D = M


@JMPHere2
0 ; JMP


(SWAP2)

@R5
D = M
@R0
M = D

@R2
D = M
@R5
M = D

@R0
D = M
@R2
M = D


(JMPHere2)


@R2
D = D - M

@SWAP2
D ; JLT



// ---- R3 dio ----


@R5
D = M


@JMPHere3
0 ; JMP


(SWAP3)

@R5
D = M
@R0
M = D

@R3
D = M
@R5
M = D

@R0
D = M
@R3
M = D


(JMPHere3)


@R3
D = D - M

@SWAP3
D ; JLT



// ---- R4 dio ----


@R5
D = M


@JMPHere4
0 ; JMP


(SWAP4)

@R5
D = M
@R0
M = D

@R4
D = M
@R5
M = D

@R0
D = M
@R4
M = D


(JMPHere4)


@R4
D = D - M

@SWAP4
D ; JLT



(END)
@END
0 ; JMP