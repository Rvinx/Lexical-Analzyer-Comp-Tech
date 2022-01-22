10 PROGRAM LISTODDNUMBER;
12 VAR num,oddnum: integer;
14 BEGIN
    20 WRITELN('List of Odd Number 1-100:');
    29 WRITELN;
    34 FOR num:=1 TO 100 DO 39 71
        39 BEGIN
        40 num1:= num MOD 2;
        42 IF (num1 <> 0) THEN 48 71
            48 Begin
            51 oddnum := num;
            54 WRITE(oddnum,' ');
        59 End;
    71 End; 34 99
99 END.
