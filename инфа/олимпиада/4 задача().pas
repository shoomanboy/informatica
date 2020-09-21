 if (k mod 2) = 0 then begin{2}
    for i := 1 to k div 2 do
    begin
      if s1[i] <> s1[k - i + 1] then begin
        delete(s, i, 1);
    k := k - 1;
        break;
      end;
    end;
    for i := 1 to k div 2 do
      if s1[i] <> s1[k - i + 1] then begin
      k := k + 1;
        break;
      end;
      break;
  end;
  
  
  
  
   if (k mod 2)<> then begin 
    for i:=1 to k div 2 do begin
        if s2[i] <> s2[k - i + 1] then begin
        delete(s2, k-i+1, 1);
    k := k - 1;
        break;
      end;
    end;
    for i := 1 to k div 2 do
      if s2[i] <> s2[k - i + 1] then begin
      k := k + 1;
        break;
      end
      else begin
        writeln(s2);                                                          {!!!!!!!!!!!!!!!!!!!!!!!!}
        k:=k+1;
        break;
      end;
  end;
  
  
  
  
  while s[i]=s[k-i+1] do  begin
  while i<=k div 2 do 
 i:=i+1;
  end;
  if i= (k div 2) then writeln(s) else writeln(s1); 
  
  
  for i:=1 to k div 2 do begin
   if s[i]<>s[k-i+1] then begin
     break;
   end;
 break;
 end;
 writeln(s1);
 for i:=1 to n div 2 do begin
   if s1[i]<>s1[n-i+1] then begin
     break;
   end;
 break;
 end;
 writeln(s2);