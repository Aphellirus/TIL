using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading;


namespace BlackJack
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Blackjack\n");
            int aces = 0;
            int sum = 0;

            var random = new Random();
            int rand = random.Next(2, 15);
            int rand2 = random.Next(2, 15);

            if(rand == 11 || rand == 12 || rand == 13)
            {
                rand = 10;
            }
            if(rand2 == 11 || rand2 == 12 || rand2 == 13)
            {
                rand2 = 10;
            }
            if(rand == 14 && rand2 == 14)
            {
                aces += 1;
                rand = 1;
                rand2 = 11;
            }
            if(rand == 14)
            {
                aces += 1;
                rand = 11;
            }
            if(rand2 == 14)
            {
                aces += 1;
                rand2 = 11;
            }

            int initCard1 = rand;
            int initCard2 = rand2;

            var cards = new List<int>() {initCard1, initCard2};
            bool session = true;
            bool stand = false;
            bool dealerStand = false;

            while(session == true)
            {
                sum = cards.Sum();
                if(sum > 21)
                {
                    if(aces > 0)
                    {
                        int aceIndex = cards.IndexOf(11);
                        cards[aceIndex] = 1;
                        aces -= 1;
                        sum = cards.Sum();
                    }
                    else
                    {
                        Console.Write("\nYour cards: ");
                        for(int i = 0; i < cards.Count; i++)
                        {
                            Console.Write(cards[i] + " ");
                        }
                        Console.WriteLine("\nYour sum is {0}", sum);
                        Console.WriteLine("You lose!");
                        session = false;
                        break;
                    }
                }
                else if(sum == 21)
                {
                    Console.Write("\nYour cards: ");
                    for(int i = 0; i < cards.Count; i++)
                    {
                        Console.Write(cards[i] + " ");
                    }
                    Console.WriteLine("\nYour sum is {0}", sum);
                    Console.WriteLine("You win!");
                    session = false;
                    break;
                }
                Console.Write("\nYour cards: ");
                for(int i = 0; i < cards.Count; i++)
                {
                    Console.Write(cards[i] + " ");
                }
                Console.WriteLine("\nYou have {0} aces", aces);
                Console.WriteLine("Your sum is {0}", sum);
                Console.WriteLine("\nHit(h) / Stand(s)");
                char choice = char.Parse(Console.ReadLine());
                if(choice == 's')
                {
                    sum = cards.Sum();
                    stand = true;
                    session = false;
                    break;
                }
                else if(choice == 'h')
                {
                    var randomCard = new Random();
                    int randCard = randomCard.Next(2, 15);
                    if(randCard == 11 || randCard == 12 || randCard == 13)
                    {
                        randCard = 10;
                    }
                    else if(randCard == 14)
                    {
                        aces += 1;
                        randCard = 11;
                    }
                    cards.Add(randCard);
                }
            }

            if(stand == true)
            {
                Console.WriteLine("\nDealer's turn");
                int dealerAces = 0;
                int dealerSum = 0;

                var dealerRandom = new Random();
                int dealerRand = dealerRandom.Next(2, 15);
                int dealerRand2 = dealerRandom.Next(2, 15);

                if(dealerRand == 11 || dealerRand == 12 || dealerRand == 13)
                {
                    dealerRand = 10;
                }
                if(dealerRand2 == 11 || dealerRand2 == 12 || dealerRand2 == 13)
                {
                    dealerRand2 = 10;
                }
                if(dealerRand == 14 && dealerRand2 == 14)
                {
                    dealerAces += 1;
                    dealerRand = 1;
                    dealerRand2 = 11;
                }
                if(dealerRand == 14)
                {
                    dealerAces += 1;
                    dealerRand = 11;
                }
                if(dealerRand2 == 14)
                {
                    dealerAces += 1;
                    dealerRand2 = 11;
                }
                int initDealerCard1 = dealerRand;
                int initDealerCard2 = dealerRand2;

                var dealerCards = new List<int>() {initDealerCard1, initDealerCard2};
                bool dealerSession = true;

                while(dealerSession == true)
                {
                    dealerSum = dealerCards.Sum();
                    if(dealerSum > 21)
                    {
                        if(dealerAces > 0)
                        {
                            int aceIndex = dealerCards.IndexOf(11);
                            dealerCards[aceIndex] = 1;
                            dealerAces -= 1;
                            dealerSum = dealerCards.Sum();
                        }
                        else
                        {
                            Console.Write("\nDealer cards: ");
                            for(int i = 0; i < dealerCards.Count; i++)
                            {
                                Console.Write(dealerCards[i] + " ");
                            }
                            Console.WriteLine("\nDealer sum is {0}", dealerSum);
                            Console.WriteLine("\nYou win!");
                            dealerSession = false;
                            break;
                        }
                    }
                    else if(sum == 21)
                    {
                        Console.Write("\nDealer cards: ");
                        for(int i = 0; i < dealerCards.Count; i++)
                        {
                            Console.Write(dealerCards[i] + " ");
                        }
                        Console.WriteLine("\nDealer sum is {0}", dealerSum);
                        dealerSession = false;
                        break;
                    }
                    Console.Write("\nDealer cards: ");
                    for(int i = 0; i < dealerCards.Count; i++)
                    {
                        Console.Write(dealerCards[i] + " ");
                    }
                    Console.WriteLine("\nDealer has {0} aces", dealerAces);
                    Console.WriteLine("Dealer sum is {0}", dealerSum);

                    char choice = 'u';
                    if(dealerSum <= 16)
                    {
                        choice = 'h';
                    }
                    else if(dealerSum >= 17)
                    {
                        choice = 's';
                    }

                    if(choice == 's')
                    {
                        Console.WriteLine("\nDealer stands\n");
                        dealerSum = dealerCards.Sum();
                        dealerStand = true;
                        dealerSession = false;
                        break;
                    }
                    else if(choice == 'h')
                    {
                        Console.WriteLine("\nDealer hits\n");
                        var randomDealerCard = new Random();
                        int randDealerCard = randomDealerCard.Next(2, 15);
                        if(randDealerCard == 11 || randDealerCard == 12 || randDealerCard == 13)
                        {
                            randDealerCard = 10;
                        }
                        else if(randDealerCard == 14)
                        {
                            dealerAces += 1;
                            randDealerCard = 11;
                        }
                        dealerCards.Add(randDealerCard);
                    }
                    Thread.Sleep(3000);
                }
                if(dealerStand == true)
                {
                    if(sum > dealerSum)
                    {
                        Console.WriteLine("\nYou win!");
                    }
                    else if(dealerSum >= sum)
                    {
                        Console.WriteLine("\nYou lose!");
                    }
                }
            }
        }
    }
}
