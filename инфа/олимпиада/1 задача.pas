program q1;
var h,A,B:integer;
i,j:integer;
begin
  readln(a,i,j);
  {a-время1 ,i- UTC первой девочки}
  {j UTC второй девочки}
  if (i>0) and (a<abs(i)) then a:=24+a-i;{1}
  if (i<0) and (a>abs(i)) then begin{2}
    a:=a+abs(i);
    if a>24 then a:=a-24;
    if a<24 then a:=a;
  end;
if (i<0) and (a<abs(i)) then a:=a+abs(i);{3}
if (i>0) and (a>i) then a:=a-i;{4}
if i=0 then a:=a;{5}
if (j<0) and (a>abs(j)) then begin {6}
       h:=a-abs(j);
       if h<0 then h:=24-abs(h);
 end;
 if j>0 then begin{7}
   h:=a+j;
   if h>24 then h:=h-24;
 end;
 if (j<0) and (a<abs(j)) then h:=24+a-abs(j);{8}
 if j=0 then h:=0;
 if h=24 then h:=0;
 writeln(h);
end.