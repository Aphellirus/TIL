def horrorDay(year)
  (1..12).count { |month| Time.new(year, month, 13).friday? }
end

year = 2021
puts horrorDay(year)
