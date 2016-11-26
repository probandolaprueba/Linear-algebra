import numpy as np;

def PowerMatrix(Matrix,Exp):
	for i in range(0,Exp-1):
		Matrix = Matrix*Matrix;
	return Matrix;

def Diagonizable(Poly,Matrix):
	LenPoly = len(Poly);
	i = 0;
	while(LenPoly != 2):
		print("sumar");
		LenPoly = LenPoly-1;
	if(LenPoly == 2):
		print("sumar B con el ultimo");
	

def main():
	print("El ingreso de la matriz es de la forma: a11 a12 ... a1N;a21 a22 ... a2N;...;aN1 aN2 ... aNN");
	MatrixString = input("Input Matrix: ");
	Matrix = np.matrix(MatrixString);
	print("A = ");
	print(Matrix);

	EigVals = np.linalg.eigvals(Matrix);
	Poly = np.poly(EigVals);
	Diagonizable(Poly,Matrix);

main();