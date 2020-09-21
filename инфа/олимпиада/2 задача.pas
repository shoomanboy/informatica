program q2;
var a,b,i:integer;
s1,s2,s:integer;
begin
  readln(a,b);
  if a>b then swap(a,b);
  for i:=a to b do begin
    if (i mod 2) =0 then s1:=s1+i
    else    s2:=s2+i;
  end;
  s:=s1-s2;
  writeln(s);
end.