ArrayList<Type> arraylistName = new ArrayList<>();

// add items to arraylist
arraylistName.add(item1);
arraylistName.add(item2);
arraylistName.add(item3);

Random random = new Random();
// random index between 0 and arraylistName.size();
int randomIndex = random.nextInt(arraylistName.size());

System.out.println(arraylistName.get(randomIndex));
