from sympy import sympify
from sympy.parsing.sympy_parser import parse_expr
from sympy import Poly
import sympy as sp
from sympy import *
import numpy as np
from fractions import Fraction
from IPython.display import display, Math

# Función para aproximar cada elemento de una lista a un cierto número de decimales
def approx_list(lst, precision):
    return [np.round(x, precision) for x in lst]


# Función para contar las repeticiones de cada elemento en una lista
def count_elements(lst):
    counter = {}
    for element in lst:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1
    return counter


def evaluate_(expr, init):
  lst = []
  for i in range(len(init)):
    lst.append(expr.subs(n, i))
  return lst

k = int(input("Enter grade of recurrence function: "))
#Listas necesarias
coeff = []
funcion =[]
n = symbols('n')
funcion = []
funcion_p=[]

#Se decide y lee el termino no homogéneo.
dec_g = int(input("Enter the non-homogeneous term type g(n): \n\t1. Constant\n\t2. Value n\n\t3. Value n^2 \n\t4. Root degree n\nYour decision:"))
if dec_g==1:
  g = int(input("Enter the value of the constant:"))
elif dec_g == 2:
  g = n
elif dec_g == 3:
  g = n**2
elif dec_g == 4:
  R = int(input("Enter the value of the Root:"))
  g = R**n
else:
  print("Enter a valid number")

#Llenado de las funciones:Homogenea y  Particular.
for i in range(k, 0, -1):
    c = int(input("Enter f(n-"+str(i)+"): "))
    coeff.append(-c)
    if c != 0:
      h = f'{str(c)}*f(n-{i})'
      funcion.append(h)
      if dec_g ==1:
        p = f'{str(c)}*c'
        funcion_p.append(p)
      elif dec_g ==2:
        p = f'{str(c)}*(A*(n-{i})+B)'
        funcion_p.append(p)
      elif dec_g == 3:
        p = f'{str(c)}*(A*(n-{i})**2+B*(n-{i})+C)'
        funcion_p.append(p)
      elif dec_g == 4:
        p= f'{str(c)}*c*{R}**(n-{i})'
        funcion_p.append(p)

# Agregar el término constante
coeff.append(1)

#Concatenacion de la funcion homogenea:
fun = ""
for i in funcion:
    fun = fun + i + " + "

#Acomodar la función que se usará y para imprimir.
fun = fun[:-3]  # Elimina el último " + " que sobra
func = parse_expr(fun)
function = fun +" + "+ str(g)
function = parse_expr(function)
print("\n The recurrent function entered is: ")

display(Math("f(n) = " +sp.latex(function)))

#Acomodar la función que se usará para resolver la parte particular.
fun_p=""

for i in funcion_p:
  fun_p = fun_p + i + " + "

fun_p = fun_p + str(g)
par = parse_expr(fun_p)

if dec_g==1:
  display(Math("c = "+sp.latex(par)))
elif dec_g == 2:
  display(Math("An + B = " +sp.latex(par)))
elif dec_g == 3:
  display(Math("An^2 + Bn + C = " +sp.latex(par)))
elif dec_g == 4:
  display(Math("c"+str(R)+"^n = " +sp.latex(par)))

#Resolver la parte homogenea para tenerlo en valores b1 y b2
coeff.reverse()
roots = np.roots(coeff)
approx_lst = approx_list(roots, 1)
approx_lst = list(np.array(approx_lst, dtype = "complex_"))
multiplicity = count_elements(approx_lst)

# Obtener los coeficientes b_i

b = symbols('b0:%d' % k)
n = symbols('n')

print("\n \nNow enter initial conditions: ")
init = []
for i in range(k):
    c = int(input(f" Enter f({i}): "))
    init.append(c)

# Obtener la expresión de la función en términos de las raíces y sus multiplicidades
expr = 0
idx = 0
ecuations = []

for root in set(approx_lst):
    m = multiplicity.get(np.round(root, 1))
    if m == 1:
        if(root == 0):
          expr += (b[idx])
        else:
          expr += (b[idx] * root**n)
        idx += 1
        ecuations.append(expr)
    else:
        poly = b[idx:idx+m][::-1]
        poly_expr = poly[0]
        for i in range(1, m):
            poly_expr += (poly[i] * n**i)
        idx += m
        if root == 0:
          ecuations.append(poly_expr)
        else:
          ecuations.append(poly_expr * root**n)
        expr += (poly_expr * root**n)

print("\nThe homogeneous equation is:")
display(Math("f_h(n) = " +sp.latex(expr))) 

print("\nThe particular equation is:")
#Esto se supone que es la forma de resolver la parte particular.
if dec_g ==1:
  c = symbols('c')
  equation = Eq(c,par)
  solution = solve(equation, c)
  sol_p = solution[0]
  expr = str(expr) + "+" +str(sol_p)
  expr = parse_expr(expr)
  display(Math("f_p(n) = " +sp.latex(sol_p)))
elif dec_g == 2:
  A, B = symbols('A B')
  equation = Eq(A*n+B,par)
  solution = solve(equation, (A,B))
  value_of_A = solution[A]
  value_of_B = solution[B]
  sol_p = f'{str(value_of_A)}*n+{str(value_of_B)}'
  sol_p = parse_expr(sol_p)
  expr = str(expr) + "+" +str(sol_p)
  expr = parse_expr(expr)
  display(Math("f_p(n) = " +sp.latex(sol_p)))
elif dec_g == 3:
  A, B, C = symbols('A B C')
  equation = Eq(A*n**2+B*n+C,par)
  solution = solve(equation, (A,B,C))
  sol_p = f'{str(solution[A])}*n**2+{str(solution[B])}*n+{str(solution[C])}'
  sol_p = parse_expr(sol_p)
  expr = str(expr) + "+" +str(sol_p)
  expr = parse_expr(expr)
  display(Math("f_p(n) = " +sp.latex(sol_p)))
elif dec_g == 4:
  c = symbols('c')
  cons = f'c*{R}**n'
  cons = parse_expr(cons)
  equation = Eq(cons,par)
  solution = solve(equation, c)
  sol_p = f'{solution[0]}*{R}**n'
  expr = str(expr) + "+" +str(sol_p)
  expr = parse_expr(expr)
  display(Math("f_p(n) = " +sp.latex(sol_p)))
##############################################################

print("\nThe function results in:")
display(Math("f(n) = " +sp.latex(expr)))

#Ultima resolución para poder tener la no recurrente.
ec = evaluate_(expr, init)
# Crear una lista con las ecuaciones resultantes de igualar cada elemento de ec con su respectiva condición inicial
eqs = [ec[i] - init[i] for i in range(len(init))]
# Resolver el sistema de ecuaciones
sol = solve(eqs, b)
# Imprimir la solución
ec_sol = expr.subs(sol)


print("\n \nThe non-recurring version of the function: \n")
display(Math("f(n) = " +sp.latex(function))) 

print("\nis as follows: \n")
display(Math("f(n) = " +sp.latex(together(powsimp(ec_sol)))))
