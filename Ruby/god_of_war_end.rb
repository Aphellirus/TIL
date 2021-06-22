class Player
    attr_accessor :name, :health, :power
    def initialize(n, h, pow)
        @name = n
        @health = h
        @power = pow
    end
    def isAlive
        @health > 0
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
        puts "#{p1.name} WON!   
        
you have defeated zeus and completed your quest for vengance
All Hail The Ghost Of Sparta        " 
    elsif p2.isAlive
        puts "#{p2.name} YOU LOST

Zeus killed you.
Dont worry it's not that death can stop you.
try again." 
    else
        puts "TIE!
       a legendary battle took place but with no victor.try again"
    end
end

def show_info(*p)
    p.each { |x| puts x}
end


puts "PLAYERS INFO"

p1 = Player.new("Kratos", 1+rand(100), 1+rand(50))
p2 = Player.new("Zeus", 5+rand(200), 2+rand(30))


show_info(p1, p2)
#made by sk sai
puts "

You are Kratos the god of war .you have set out to finally defeat zeus once and for all in the final battle.can u get vengeance or will u be killed(again)


********************************
Pandora: There it is; I can see it Kratos! In the darkness, the fires of Hope will set us free! (she tries to run for the Flame, but Kratos grabs her wrist)

Kratos: Pandora, no

Pandora: You know why I'm here. You brought me here to do this!Kratos: I will find another way!Pandora: No, Kratos There is no other way-Let me go (she tries to struggle free)

Kratos: NO, CHILD

Pandora: I am not a child! You're hurting me! (she pulls free of Kratos and heads for the Flame, only to run headlong into Zeus. Pandora screams as Zeus seizes her by the throat) Kratos, help!
Kratos: Put her down, Zeus

Zeus: Your obsession with this...this thing has become somewhat of a nuisance, my son.
Kratos: Release the girl, Zeus!!

Zeus: Don't confuse this...object, this construction of Hephaestus with your own flesh and blood! (mockingly, as he sees the glare on Kratos' face) But perhaps you already have, Spartan. Your quest for Pandora - your pathetic attempt for atonement from the family you slaughtered - has caused nothing but havoc on Olympus! [gestures to the destruction around them] Look around at what you have done!

Kratos: (coldly) I see only what I have come to destroy.

Zeus: Taking pity on you has been my greatest mistake, Kratos. Just as taking pity on this thing will prove to be your greatest mistake

Kratos: This has nothing to do with her

Zeus: (holding Pandora above his head) It has everything to do with her

Kratos: (draws his blades) PUT HER DOWN

Zeus: As you wish (Zeus hurls Pandora aside, and he and Kratos hurl themselves into each other)

(Trying to stop Pandora from going to the Flames of Olympus)

Kratos: Pandora

Zeus: Stop her, Kratos! Don't let her go into the flames

Pandora: This is what i meant do to! You know that 
Please

Zeus: Hush

Pandora: Kratos, you Know this is the only way.

Zeus: Don't listen to her, 
Kratos. For once in your pathetic life, don't fail. Don't fail her like you failed your family. 

********************************

NOW FIGHT!!

"
#made by Neptuos
fight(p1, p2)
