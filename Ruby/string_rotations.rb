x = gets.chomp
result = []
x.each_char do
 x = x[1..x.size] + x[0]
 result << x
end
puts result
