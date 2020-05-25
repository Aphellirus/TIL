x = gets.to_i
y = 0

while x != 0 do
    y = y*10
    y = y + (x%10)
    x = x/10 

  puts y      
end
