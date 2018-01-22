solve_qe: obj/solve_qe.o obj/qe.o
	gcc obj/solve_qe.o obj/qe.o -o bin/solve_qe.out

obj/solve_qe.o: src/solve_qe.c
	gcc -c src/solve_qe.c -o obj/solve_qe.o

obj/qe.o: lib/qe.c
	gcc -c lib/qe.c -o obj/qe.o
