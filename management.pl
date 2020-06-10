
flight(toronto,airCanada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(toronto,airCanada,london,500,360).
flight(toronto,united,london,650,420).
flight(madrid,airCanada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,malaga,50,60).
flight(madrid,iberia,valencia,40,50).
flight(malaga,iberia,valencia,80,120).
flight(barcelona,iberia,valencia,110,75).
flight(paris,united,toulouse,35,120).
flight(barcelona,iberia,london,220,240).

airport(toronto,50,60).
airport(madrid,75,45).
airport(valencia,40,20).
airport(malaga,50,30).
airport(barcelona,40,30).
airport(paris,50,60).
airport(london,75,80).
airport(toulouse,40,30).

isFlight(A, B) :-
	flight(A, C, B, D, E);
	flight(B, C, A, D, E).

isCheap(A, C, B) :-
	flight(A, C, B, D, E),
	D < 400.

preferrable(A, C, B) :-
	isCheap(A, C, B);
	C == airCanada.

isUnited(A, B) :-
	flight(A, C, B, D, E),
	C == united.

isAirCanada(A, B) :-
	flight(A, C, B, D, E),
	C == airCanada.

ifElse(A, B) :-
	isUnited(A, B),
	isAirCanada(A, B).


twoFlight(paris, toronto) :-
	write('yes').

flightPrint(A, C, B, P, D) :-
    flight(A, C, B, P, D),
    write('A = '),
    write(B),
    nl,
    write('C = '),
    write(C),
    nl,
    write('B = '),
    write(A),
    nl,
    write('P = '),
    write(P),
    write($),
    nl,
    write('D = '),
    write(D),
    write(m),
    nl.


%query(A,C,B) :- X=united,ifElse(A,X,B,D,E),C=airCanada.

