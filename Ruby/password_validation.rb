str=gets                  
str=str.downcase
c1,c2 = 0,0               
for x in 0...str.length
a=str [x]
  case a
    when '0'..'9'
       c1 +=1
    when '@','#','%','&','$','!','*'
       c2 +=1
  end 
end
if (c1 > 1) && (c2 > 1) && (str.length > 6)
  puts 'Strong'
else
  puts 'Weak'
end
