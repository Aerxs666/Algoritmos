Proceso AlgoritmoTablas
	definir tablar Como Entero;
	Escribir  "Ingresa el numero de la tabla que deseas saber (Del 1 al 11): ";
	leer tablar;
	tabla1 = "Tabla del 1: 1 x 2 = 2 1 x 3 = 31 x 4 = 41 x 5 = 51 x 6 = 61 x 7 = 71 x 8 = 81 x 9 = 91 x 10 = 10";
	tabla2 = "Tabla del 2: 2 x 2 = 4 2 x 3 = 6 2 x 4 = 8 2 x 5 = 10 2 x 6 = 12 2 x 7 = 14 2 x 8 = 16 2 x 9 = 18 2 x 10 = 20";
	tabla3 ="Tabla del 3: 3 x 2 = 6 3 x 3 = 9 3 x 4 = 12 3 x 5 = 15 3 x 6 = 18 3 x 7 = 21 3 x 8 = 24 3 x 9 = 27 3 x 10 = 30";
	tabla4 ="Tabla del 4: 4 x 2 = 8 4 x 3 = 12 4 x 4 = 16 4 x 5 = 20 4 x 6 = 24 4 x 7 = 28 4 x 8 = 32 4 x 9 = 36 4 x 10 = 40";
	tabla5 ="Tabla del 5: 5 x 2 = 10 5 x 3 = 15 5 x 4 = 20 5 x 5 = 25 5 x 6 = 30 5 x 7 = 35 5 x 8 = 40 5 x 9 = 45 5 x 10 = 50";
	tabla6 ="Tabla del 6: 6 x 2 = 12 6 x 3 = 18 6 x 4 = 24 6 x 5 = 30 6 x 6 = 36 6 x 7 = 42 6 x 8 = 48 6 x 9 = 54 6 x 10 = 60";
	tabla7 = "Tabla del 7: 7 x 2 = 14 7 x 3 = 21 7 x 4 = 28 7 x 5 = 35 7 x 6 = 42 7 x 7 = 49 7 x 8 = 56 7 x 9 = 63 7 x 10 = 70";
	tabla8 ="Tabla del 8: 8 x 2 = 16 8 x 3 = 24 8 x 4 = 32 8 x 5 = 40 8 x 6 = 48 8 x 7 = 56 8 x 8 = 64 8 x 9 = 72 8 x 10 = 80";
	tabla9 ="Tabla del 9: 9 x 2 = 18 9 x 3 = 27 9 x 4 = 36 9 x 5 = 45 9 x 6 = 54 9 x 7 = 63 9 x 8 = 72 9 x 9 = 81 9 x 10 = 90";
	tabla10 ="Tabla del 10: 10 x 2 = 20 10 x 3 = 30 10 x 4 = 40 10 x 5 = 50 10 x 6 = 60 10 x 7 = 70 10 x 8 = 80 10 x 9 = 90 10 x 10 = 100";
	tabla11 ="Tabla del 11: 11 x 2 = 22 11 x 3 = 33 11 x 4 = 44 11 x 5 = 55 11 x 6 = 66 11 x 7 = 77 11 x 8 = 88 11 x 9 = 99 11 x 10 = 110";
	Mientras tablar >11 Hacer
		Mostrar "Es del 1 al 11 imbecil"
	FinMientras
	si tablar == 1 Entonces
		Mostrar tabla1
	FinSi
	si tablar == 2 Entonces
		Mostrar tabla2
	FinSi
	si tablar == 3 Entonces
		Mostrar tabla3
	FinSi
	si tablar == 4 Entonces
		Mostrar tabla4
	FinSi
	si tablar == 5 Entonces
		Mostrar tabla5
	FinSi
	si tablar == 6 Entonces
		Mostrar tabla6
	FinSi
	si tablar == 7 Entonces
		Mostrar tabla7
	FinSi
	si tablar == 8 Entonces
		Mostrar tabla8
	FinSi
	si tablar == 9 Entonces
		Mostrar tabla9
	FinSi
	si tablar == 10 Entonces
		Mostrar tabla10
	FinSi
	si tablar == 11 Entonces
		Mostrar tabla11
	FinSi
FinProceso
