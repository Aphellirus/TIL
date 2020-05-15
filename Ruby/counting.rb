begin
    n = gets.chomp 
    
    unless Integer(n) 
        raise ArgumentError
    else
        n = n.to_i 
        
        1.upto(n) { | n | puts n }
        
        a = n - 1
        
        while a > 0
            puts a
            a = a - 1
        end
    end
rescue ArgumentError => e  
    puts "You messed up!, Enter a valid Integer."
end
