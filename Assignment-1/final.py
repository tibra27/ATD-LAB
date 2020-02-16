import ply.lex as lex
import ply.yacc as yacc
from node import node

#TOKENS
tokens=('SELECT','FROM','WHERE','ORDER_BY','GROUP_BY','HAVING','NAME','AND','OR','COMMA','TABLE',
'EQUALS','CONDITION','SPACE','LP','RP','JOIN','AVG','BETWEEN','IN','SUM','MAX','MIN','COUNT','UNION','INTERSECT',
'EXCEPT','NUMBER','ATTR','NATURAL_JOIN','INSERT','INTO','VALUES','DELETE','ANY','ALL','UPDATE','SET','INV','AS','DOT','DISTINCT','DROP','CREATE','float','char','varchar','int')

literals = ['=','+','-','*', '^','>','<' ]
#DEF OF TOKENS

def t_TABLE(t):
	r'TABLE'
	return t

def t_DROP(t):
	r'DROP'
	return t

def t_CREATE(t):
	r'CREATE'
	return t

def t_int(t):
	r'int'
	return t

def t_float(t):
	r'float'
	return t

def t_char(t):
	r'char'
	return t

def t_varchar(t):
	r'varchar'
	return t

def t_LP(t):
	r'\('
	return t

def t_JOIN(t):
	r'JOIN'
	return t
def t_DISTINCT(t):
	r'DISTINCT'
	return t

def t_DOT(t):
	r'\.'
	return t

def t_AS(t):
	r'AS'
	return t

def t_UPDATE(t):
	r'UPDATE'
	return t
def t_SET(t):
	r'SET'
	return t

def t_ANY(t):
	r'ANY'
	return t

def t_ALL(t):
	r'ALL'
	return t

def t_DELETE(t):
	r'DELETE'
	return t


def t_INSERT(t):
	r'INSERT'
	return t

def t_VALUES(t):
	r'VALUES'
	return t

def t_INTO(t):
	r'INTO'
	return t


def t_UNION(t):
	r'UNION'
	return t


def t_INTERSECT(t):
	r'INTERSECT'
	return t

def t_EXCEPT(t):
	r'EXCEPT'
	return t

def t_SUM(t):
	r'SUM'
	return t

def t_MIN(t):
	r'MIN'
	return t

def t_MAX(t):
	r'MAX'
	return t
def t_COUNT(t):
	r'COUNT'
	return t

def t_AVG(t):
	r'AVG'
	return t

def t_RP(t):
	r'\)'
	return t

def t_BETWEEN(t):
	r'BETWEEN'
	return t

def t_IN(t):
	r'IN'
	return t

def t_SELECT(t):
	r'SELECT'
	return t

def t_FROM(t):
	r'FROM'
	return t

def t_WHERE(t):
	r'WHERE'
	return t

def t_ORDER_BY(t):
	r'ORDER_BY'
	return t

def t_GROUP_BY(t):
	r'GROUP_BY'
	return t

def t_HAVING(t):
	r'HAVING'
	return t

def t_OR(t):
	r'OR'
	return t

def t_AND(t):
	r'AND'
	return t

def t_COMMA(t):
	r','
	return t

def t_NATURAL_JOIN(t):
	r'NATURAL_JOIN'
	return t


def t_CONDITION(t):
	r'[a-zA-Z0-9_]+[\t]*[=\+-><][\t]*[a-zA-Z0-9_]+[\t]*[AND]*[OR]*'
	return t
def t_INV(t):
	r'\"'
	return t


def t_NUMBER(t):
	r'[0-9]+'
	return t

def t_NAME(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*|[A-Z]*\.[A-Z]$'

	return t

def t_ATTR(t):
#	r'[a-zA-Z0-9_]\.[a-zA-Z0-9_]+'
	r'([0-9]*\.[0-9]+|[0-9]+)'
	print("attr")
	print(t)
	return t

# Ignored characters
t_ignore = " \t"
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# LEXICAL ANALYSIS
lex.lex()

#PARSING GRAMMAR

def p_query(t):
	'''query :  select
			| groupquery
			| LP query RP
			| insert
			| delete
			| update
			| drop
			| create
			'''
	if len(t)==2:
		t[0]=node('[QUERY]')
		t[0].add(t[1])
	else:
		t[0]=node('[QUERY]')
		t[0].add(t[2])


def p_table(t):
	'''table : NAME
			|  LP query	RP
			| NAME AS NAME
			| table COMMA table'''
	if len(t)==2:
		t[0]=node('[TABLE]')
		t[0].add(node(t[1]))
	elif t[2]=='AS':
		t[0]=node('[TABLE]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
		t[0].add(node(t[3]))
	elif t[2]==',':
		t[0]=node('[TABLE]')
		t[0].add(t[1])
		t[0].add(t[2])
		t[0].add(t[3])
	else :
		t[0]=node('[TABLE]')
		t[0].add(node('('))
		t[0].add(t[2])
		t[0].add(node(')'))


def p_select(t):
	'''select : SELECT list FROM table where
				| SELECT DISTINCT list FROM table where'''
	if(t[2]=='DISTINCT'):
		t[0]=node('[SELECT]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(t[3])
		t[0].add(node(t[4]))
		t[0].add(t[5])
		t[0].add(t[6])
	else:
		t[0]=node('[SELECT]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
		t[0].add(node(t[3]))
		t[0].add(t[4])
		t[0].add(t[5])
		

	

def p_where(t):
	''' where : WHERE lst order
			 | order
			 | '''
	if len(t)==3 and t[1]=='WHERE' :
		t[0]=node('[WHERE]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
	elif len(t)==2:
		t[0]=node('[WHERE]')
		t[0].add(t[1])


	elif len(t)==4:
		t[0]=node('[WHERE]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
		t[0].add(t[3])
	else:
		t[0]=node('[WHERE]')
		t[0].add(node('empty'))


def p_order(t):
	''' order : ORDER_BY list
				|
			  '''
	if(len(t)==3):
		t[0]=node('[ORDER]')
		t[0].add(node('ORDER_BY'))
		t[0].add(t[2])

	else:
		t[0]=node('[ORDER]')
		t[0].add(node('empty'))


def p_groupquery(t):
	''' groupquery : SELECT list FROM table where group '''
	t[0]=node('GROUP_QUERY')
	t[0].add(node(t[1]))
	t[0].add(t[2])
	t[0].add(node(t[3]))
	t[0].add(t[4])
	t[0].add(t[5])
	t[0].add(t[6])


def p_lst(t):
	''' lst  : condition
			  | condition AND condition
			  | condition OR condition
			  | NAME BETWEEN NUMBER AND NUMBER
			  | NAME IN LP query RP
		 | NAME '<' agg
		 | NAME '>' agg
		 | agg '>' NUMBER
		 | NAME '=' agg
		 | agg '=' NUMBER
		 | agg '<' NUMBER
			  '''

	if len(t)==2:
		t[0]=node('[LST]')
		t[0].add(t[1])
	elif t[2]==',':
		t[0]=node('[LST]')
		t[0].add(t[1])
		t[0].add(t[3])
	elif t[2]=='AND':
		t[0]=node('[LST]')
		t[0].add(t[1])
		t[0].add(node('AND'))
		t[0].add(t[3])
	elif t[2]=='OR':
		t[0]=node('[LST]')
		t[0].add(t[1])
		t[0].add(node('OR'))
		t[0].add(t[3])
	elif t[2]=='BETWEEN':
		temp='%s >= %s & %s <= %s'%(t[1],str(t[3]),t[1],str(t[5]))
		t[0]=node('[LST]')
		t[0].add(node('[TERM]'))
		t[0].add(node(temp))
	elif t[2]=='IN':
		t[0]=node('[LST]')
		t[0].add(node(t[1]))
		t[0].add(node('IN'))
		t[0].add(t[4])
	elif t[2]=='<' and len(t)==4:
		t[0]=node('[LST]')
		if isinstance(t[1], node) :
			t[0].add(t[1])
		else :
			t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		if isinstance(t[3], node) :
			t[0].add(t[3])
		else :
			t[0].add(node(t[3]))
	elif t[2]=='=' and len(t)==4:
		
		t[0]=node('[LST]')
		if isinstance(t[1], node) :
			t[0].add(t[1])
		else :
			t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		if isinstance(t[3], node) :
			t[0].add(t[3])
		else :
			t[0].add(node(t[3]))
	elif t[2]=='>' and len(t)==4:
		
		t[0]=node('[LST]')
		if isinstance(t[1], node) :
			t[0].add(t[1])
		else :
			t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		if isinstance(t[3], node) :
			t[0].add(t[3])
		else :
			t[0].add(node(t[3]))
	else:
		t[0]=node('')


def p_condition(t):
	''' condition : NAME '>' NUMBER
					| NAME '>' agg
					| NAME '<' NUMBER
					| NAME '<' agg
					| NAME '=' NUMBER
					| NAME '=' agg
					| NAME '>' NAME
					| NAME '<' NAME
					| NAME '=' NAME
					| list '>' list
					| list '<' list
					| list '=' list
					| NAME '=' INV NAME INV  '''
	if len(t)==4:
		t[0]=node('[CONDITION]')
		if isinstance(t[1], node) :
			t[0].add(t[1])
		else :
			t[0].add(node(str(t[1])))
			t[0].add(node(t[2]))
		if isinstance(t[3], node) :
			t[0].add(t[3])
		else :
			t[0].add(node(str(t[3])))
	else:
		t[0]=node('[CONDITION]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))
		t[0].add(node(t[4]))
		t[0].add(node(t[5]))


def p_group(t):
	''' group :  GROUP_BY listg
			 |
			  '''
	if len(t)==3:
		t[0]=node('[GROUP]')
		t[0].add(node('GROUP_BY'))
		t[0].add(t[2])
	else:
		t[0]=node('[GROUP]')
		t[0].add(node('empty'))


def p_agg(t):
	''' agg : SUM LP NAME RP
			| AVG LP NAME RP
			| COUNT LP NAME RP
			| MIN LP NAME RP
			| MAX LP NAME RP
			| COUNT LP '*' RP
		'''

	t[0]=node('[AGGREGATE]')
	t[0].add(node(t[1]))
	t[0].add(node('('))
	t[0].add(node(t[3]))
	t[0].add(node(')'))

def p_list(t):
	''' list  : '*'
				| NAME
				| NAME DOT NAME
			  | list COMMA list
			| agg
			  '''
	if len(t)==2:
		t[0]=node('[LIST]')
		if isinstance(t[1], node) :
			t[0].add(t[1])
		else:
			t[0].add(node(t[1]))
	elif t[2]==',':
		t[0]=node('[LIST]')
		t[0].add(t[1])
		t[0].add(node(t[2]))
		t[0].add(t[3])
	else:
		t[0]=node('[LIST]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))



def p_listg(t):
	''' listg  : NAME
			  | listg COMMA NAME
			  | listg AND NAME
			  | listg OR NAME


			  '''
	if len(t)==2:
		t[0]=node('[LISTG]')
		t[0].add(node(t[1]))
	else:
		t[0]=node('[LISTG]')
		t[0].add(t[1])
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))


def p_error(t):
	print("Syntax error at '%s'" % t.value)



# insert
def p_insert(t):
	''' insert :  INSERT INTO NAME VALUES LP data RP
			| INSERT INTO NAME LP data RP VALUES LP data RP'''
	if (len(t)==8):
		t[0]=node('[INSERT]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))
		t[0].add(node(t[4]))
		t[0].add(node('('))
		t[0].add(t[6])
		t[0].add(node(')'))
	else:
		t[0]=node('[INSERT]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))
		t[0].add(node('('))
		t[0].add(t[5])
		t[0].add(node(')'))
		t[0].add(node(t[7]))
		t[0].add(node('('))
		t[0].add(t[9])
		t[0].add(node(')'))
def p_data(t):
	''' data : NUMBER
			| NAME
			| INV NAME INV
			| data COMMA data
	'''
	if len(t)==2:
		t[0]=node('[DATA]')
		t[0].add(node(t[1]))
	elif(t[2]==','):
		t[0]=node('[DATA]')
		t[0].add(t[1])
		t[0].add(node(t[2]))
		t[0].add(t[3])
	else :
		t[0]=node('[DATA]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))

def p_delete(t):
	''' delete :  DELETE FROM table
			| DELETE FROM table WHERE condition'''
	if len(t)==6:
			t[0]=node('[DELETE]')
			t[0].add(node(t[1]))
			t[0].add(node(t[2]))
			t[0].add(t[3])
			t[0].add(node(t[4]))
			t[0].add(t[5])
	else:
			t[0]=node('[DELETE]')
			t[0].add(node(t[1]))
			t[0].add(node(t[2]))
			t[0].add(t[3])

def p_update(t):
	''' update : UPDATE NAME SET query3
			| UPDATE NAME SET query3 WHERE condition
			'''
	if len(t)==7:
			t[0]=node('[UPDATE]')
			t[0].add(node(t[1]))
			t[0].add(node(t[2]))
			t[0].add(node(t[3]))
			t[0].add(t[4])
			t[0].add(node(t[5]))
			t[0].add(t[6])
	else:
			t[0]=node('[UPDATE]')
			t[0].add(node(t[1]))
			t[0].add(node(t[2]))
			t[0].add(node(t[3]))
			t[0].add(t[4])
def p_query3(t):
	''' query3 : NAME '=' expression COMMA query3
					| NAME '=' expression '''
	if (len(t)==4):
		t[0]=node('[QUERY3]')
		t[0].add(node(t[1]))
		t[0].add(node('='))
		t[0].add(t[3])
	else:
		t[0]=node('[QUERY3]')
		t[0].add(node(t[1]))
		t[0].add(node('='))
		t[0].add(t[3])
		t[0].add(node(','))
		t[0].add(t[5])

def p_expression(t):
	'''expression : NUMBER '+' NUMBER
				  | NUMBER '-' NUMBER
				  | NUMBER '*' NUMBER
				  | NUMBER '/' NUMBER
				  | INV NAME INV
		  | NAME
			| NUMBER'''
	if len(t)==2:
		t[0]=node('[EXPRESSION]')
		t[0].add(node(t[1]))
	else:
		t[0]=node('[EXPRESSION]')
		t[0].add(node(t[1]))
		t[0].add(node(t[2]))
		t[0].add(node(t[3]))


def p_drop(t):
	''' drop : DROP TABLE NAME '''
	t[0]=node('[DROP]')
	t[0].add(node(t[1]))
	t[0].add(node(t[2]))
	t[0].add(node(t[3]))

def p_create(t):
	''' create : CREATE TABLE NAME LP query2 RP '''
	t[0]=node('[CREATE]')
	t[0].add(node(t[1]))
	t[0].add(node(t[2]))
	t[0].add(node(t[3]))
	t[0].add(node('('))
	t[0].add(t[5])
	t[0].add(node(')'))
def p_query2(t):
	''' query2 : NAME dtype COMMA query2
				| NAME dtype '''
	if (len(t)==3):
		t[0]=node('[QUERY2]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
	else:
		t[0]=node('[QUERY2]')
		t[0].add(node(t[1]))
		t[0].add(t[2])
		t[0].add(node(','))
		t[0].add(t[4])
		
def p_dtype(t):
	''' dtype : int
	| char
	| varchar
	| float '''
	t[0]=node('[DTYPE]')
	t[0].add(node(t[1]))

yacc.yacc()



while 1:
	try:
		s = input('-> ')
		pass
	except EOFError:
		break
	a=yacc.parse(s)
	a.print_node(0)

