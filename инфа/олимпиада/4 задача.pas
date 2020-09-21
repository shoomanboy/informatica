program q3;

var
  i, k,s3,s4,j,n: integer;
  s, s1, s2: string;
begin
  readln(s);
  s1 := s;
  s2:=s;
  for i := 1 to length(s) do
  begin
    k := k + 1;
  end;
  n:=k;
  j:=n;
  {___________________1111111____________________}
    for i := 1 to k div 2 do
    begin
      if s[i] <> s[k - i + 1] then begin
        delete(s, k - i + 1, 1);
            k := k - 1;
        break;
      end;     
    end;
    for i := 1 to k div 2 do
      if s[i] <> s[k - i + 1] then begin
        break;
        end else begin
          k:=k+1;
          break;
        end;
{_________________222222_________________________}
    for i := 1 to n div 2 do
    begin
      if s1[i] <> s1[n - i + 1] then begin
        delete(s1, i, 1);
           n := n - 1;
        break;
      end;
    end;
    for i := 1 to n div 2 do
      if s1[i] <> s1[n - i + 1] then begin
        break;
        end 
        else begin
          n:=n+1;
          break;
        end;
  
  {_____________________333333_____________________}
 n:=0;
 for i:=1 to (j-1) div 2 do begin
   if s[i]=s[j-i] then s3:=s3+1;
   end;
   if s3= (j-1) div 2 then begin
   for j:=1 to length(s) do n:=n+1;
   writeln(n);
   end 
   else writeln(0);
   


end.