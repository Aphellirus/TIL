 puts ""
name = gets.chomp
puts "Welcome, #{name}"
class Player
    attr_accessor :name, :health, :power
    def initialize(n, h, pow)
        @name = n
        @health = h
        @power = pow
    end
    def isAlive
        @health > 5
    end
    def hit(opponent)
        opponent.health -= self.power
    end
    def to_s
        "#{name}: Health: #{health}, Power: #{power}"
    end
end

def fight(p1, p2)
    while p1.isAlive && p2.isAlive
        p1.hit(p2)
        p2.hit(p1)
        
        show_info(p1, p2)
    end
    
    if p1.isAlive 
    puts""
        puts "**The WINNER IS ... #{p1.name} :)** " 
    elsif p2.isAlive
    puts""
        puts "**Sorry...The WINNER IS ... #{p2.name} :(**" 
    else
    puts""
        puts "**IT'S TIE! O_o **"
    end
end

def show_info(*p)
    p.each { |x| puts x}
end

#initialize Players
puts "PLAYERS INFO"
puts ""
p1 = Player.new("YOU", 1+rand(100), 1+rand(20))
p2 = Player.new("Computer", 1+rand(100), 1+rand(20))

#show Player info
show_info(p1, p2)
puts ""
puts "ALRIGHT #{name} LETS FIGHT [wait...... you cant fight to your own computer] :/ but you had run my code !! so just watch it who wins ??  " 
puts ""
fight(p1, p2)
