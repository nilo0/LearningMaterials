all: link

compile:
	@gcc -c ./src/solve_qe.c ./lib/qe.c
	@mv ./solve_qe.o ./obj
	@mv ./qe.o ./obj

link: compile
	@gcc ./obj/solve_qe.o ./obj/qe.o -o ./bin/solve_qe.out
