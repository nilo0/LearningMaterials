bin/solve_qe.out: obj/solve_qe.o obj/qe.o
	gcc $^ -o $@

obj/solve_qe.o: src/solve_qe.c
	gcc -c $< -o $@

obj/qe.o: lib/qe.c
	gcc -c $< -o $@
