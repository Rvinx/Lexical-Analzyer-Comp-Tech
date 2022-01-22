
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN COLON COMMA DATA DIVIDE DOT END EQUALS FLOAT ID INTEGER LPAREN MINUS NEWLINE PLUS POWER PROGRAM RPAREN SEMI STRING TIMES VAR WRITE WRITELNprogram : program statement\n               | statementprogram : errorstatement : INTEGER command NEWLINEstatement : INTEGER error NEWLINEstatement : NEWLINEstatement : INTEGER NEWLINEcommand : DATA numlistcommand : DATA errorcommand : WRITELN LPAREN wlist RPAREN endingcommand : WRITELN errorcommand : WRITELN LPAREN RPAREN endingcommand : WRITE LPAREN wlist RPAREN endingcommand : WRITE errorcommand : WRITE LPAREN RPAREN endingcommand : PROGRAM variable endingcommand : VAR varlist COLON variable endingcommand : VAR errorcommand : variable COLON variable endingcommand : variable errorcommand : variable COLON EQUALS expr SEMIvarlist : varlist COMMA variable\n               | variableexpr : INTEGER\n            | FLOATexpr : variableexpr : expr PLUS expr\n            | expr MINUS expr\n            | expr TIMES expr\n            | expr DIVIDE expr\n            | expr POWER exprvariable : IDcommand : END DOTcommand : BEGINending : SEMIwlist   : wlist COMMA ID\n               | witemwitem : STRINGnumlist : numlist COMMA number\n               | numbernumber  : INTEGER\n               | FLOAT'
    
_lr_action_items = {'error':([0,4,10,11,12,14,15,18,],[3,9,22,27,29,32,35,-32,]),'INTEGER':([0,1,2,3,5,6,8,10,19,20,37,47,67,68,69,70,71,],[4,4,-2,-3,-6,-1,-7,24,-4,-5,24,59,59,59,59,59,59,]),'NEWLINE':([0,1,2,3,4,5,6,7,8,9,17,19,20,21,22,23,24,25,27,29,32,35,36,44,45,50,53,55,56,63,65,66,72,],[5,5,-2,-3,8,-6,-1,19,-7,20,-34,-4,-5,-8,-9,-40,-41,-42,-11,-14,-20,-18,-33,-16,-35,-39,-12,-15,-19,-10,-13,-21,-17,]),'$end':([1,2,3,5,6,8,19,20,],[0,-2,-3,-6,-1,-7,-4,-5,]),'DATA':([4,],[10,]),'WRITELN':([4,],[11,]),'WRITE':([4,],[12,]),'PROGRAM':([4,],[13,]),'VAR':([4,],[15,]),'END':([4,],[16,]),'BEGIN':([4,],[17,]),'ID':([4,13,15,31,47,48,49,52,67,68,69,70,71,],[18,18,18,18,18,18,18,64,18,18,18,18,18,]),'FLOAT':([10,37,47,67,68,69,70,71,],[25,25,60,60,60,60,60,60,]),'LPAREN':([11,12,],[26,28,]),'COLON':([14,18,33,34,62,],[31,-32,48,-23,-22,]),'DOT':([16,],[36,]),'SEMI':([18,30,39,43,46,51,54,57,58,59,60,61,73,74,75,76,77,],[-32,45,45,45,45,45,45,-26,66,-24,-25,45,-27,-28,-29,-30,-31,]),'COMMA':([18,21,23,24,25,33,34,38,40,41,42,50,62,64,],[-32,37,-40,-41,-42,49,-23,52,-37,-38,52,-39,-22,-36,]),'PLUS':([18,57,58,59,60,73,74,75,76,77,],[-32,-26,67,-24,-25,67,67,67,67,67,]),'MINUS':([18,57,58,59,60,73,74,75,76,77,],[-32,-26,68,-24,-25,68,68,68,68,68,]),'TIMES':([18,57,58,59,60,73,74,75,76,77,],[-32,-26,69,-24,-25,69,69,69,69,69,]),'DIVIDE':([18,57,58,59,60,73,74,75,76,77,],[-32,-26,70,-24,-25,70,70,70,70,70,]),'POWER':([18,57,58,59,60,73,74,75,76,77,],[-32,-26,71,-24,-25,71,71,71,71,71,]),'RPAREN':([26,28,38,40,41,42,64,],[39,43,51,-37,-38,54,-36,]),'STRING':([26,28,],[41,41,]),'EQUALS':([31,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,6,]),'command':([4,],[7,]),'variable':([4,13,15,31,47,48,49,67,68,69,70,71,],[14,30,34,46,57,61,62,57,57,57,57,57,]),'numlist':([10,],[21,]),'number':([10,37,],[23,50,]),'varlist':([15,],[33,]),'wlist':([26,28,],[38,42,]),'witem':([26,28,],[40,40,]),'ending':([30,39,43,46,51,54,61,],[44,53,55,56,63,65,72,]),'expr':([47,67,68,69,70,71,],[58,73,74,75,76,77,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program statement','program',2,'p_program','PascalParse.py',16),
  ('program -> statement','program',1,'p_program','PascalParse.py',17),
  ('program -> error','program',1,'p_program_error','PascalParse.py',33),
  ('statement -> INTEGER command NEWLINE','statement',3,'p_statement','PascalParse.py',40),
  ('statement -> INTEGER error NEWLINE','statement',3,'p_statement_bad','PascalParse.py',55),
  ('statement -> NEWLINE','statement',1,'p_statement_newline','PascalParse.py',62),
  ('statement -> INTEGER NEWLINE','statement',2,'p_statement_blank','PascalParse.py',73),
  ('command -> DATA numlist','command',2,'p_command_data','PascalParse.py',77),
  ('command -> DATA error','command',2,'p_command_data_bad','PascalParse.py',82),
  ('command -> WRITELN LPAREN wlist RPAREN ending','command',5,'p_command_writeln','PascalParse.py',88),
  ('command -> WRITELN error','command',2,'p_command_writeln_bad','PascalParse.py',93),
  ('command -> WRITELN LPAREN RPAREN ending','command',4,'p_command_writeln_empty','PascalParse.py',97),
  ('command -> WRITE LPAREN wlist RPAREN ending','command',5,'p_command_write','PascalParse.py',102),
  ('command -> WRITE error','command',2,'p_command_write_bad','PascalParse.py',107),
  ('command -> WRITE LPAREN RPAREN ending','command',4,'p_command_write_empty','PascalParse.py',111),
  ('command -> PROGRAM variable ending','command',3,'p_command_program','PascalParse.py',116),
  ('command -> VAR varlist COLON variable ending','command',5,'p_command_var','PascalParse.py',124),
  ('command -> VAR error','command',2,'p_command_var_error','PascalParse.py',129),
  ('command -> variable COLON variable ending','command',4,'p_command_declare','PascalParse.py',134),
  ('command -> variable error','command',2,'p_command_declare_error','PascalParse.py',139),
  ('command -> variable COLON EQUALS expr SEMI','command',5,'p_command_assign','PascalParse.py',144),
  ('varlist -> varlist COMMA variable','varlist',3,'p_command_varlist','PascalParse.py',149),
  ('varlist -> variable','varlist',1,'p_command_varlist','PascalParse.py',150),
  ('expr -> INTEGER','expr',1,'p_command_value','PascalParse.py',158),
  ('expr -> FLOAT','expr',1,'p_command_value','PascalParse.py',159),
  ('expr -> variable','expr',1,'p_command_variable','PascalParse.py',163),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binary','PascalParse.py',167),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binary','PascalParse.py',168),
  ('expr -> expr TIMES expr','expr',3,'p_expr_binary','PascalParse.py',169),
  ('expr -> expr DIVIDE expr','expr',3,'p_expr_binary','PascalParse.py',170),
  ('expr -> expr POWER expr','expr',3,'p_expr_binary','PascalParse.py',171),
  ('variable -> ID','variable',1,'p_variable','PascalParse.py',177),
  ('command -> END DOT','command',2,'p_command_end','PascalParse.py',181),
  ('command -> BEGIN','command',1,'p_command_begin','PascalParse.py',186),
  ('ending -> SEMI','ending',1,'p_ending','PascalParse.py',192),
  ('wlist -> wlist COMMA ID','wlist',3,'p_wlist','PascalParse.py',199),
  ('wlist -> witem','wlist',1,'p_wlist','PascalParse.py',200),
  ('witem -> STRING','witem',1,'p_item_string','PascalParse.py',209),
  ('numlist -> numlist COMMA number','numlist',3,'p_numlist','PascalParse.py',220),
  ('numlist -> number','numlist',1,'p_numlist','PascalParse.py',221),
  ('number -> INTEGER','number',1,'p_number','PascalParse.py',233),
  ('number -> FLOAT','number',1,'p_number','PascalParse.py',234),
]
