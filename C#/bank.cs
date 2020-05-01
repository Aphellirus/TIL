using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
// Compiler version 4.0, .NET Framework 4.5

class Account
{
  private decimal balance;
  
  public void deposit(decimal depositAmount)
  {
    balance += depositAmount;
    Console.WriteLine($"${depositAmount} have been deposited to your account.\n");
  }
  
  public void withdraw(decimal withdrawAmount)
  {
    if(withdrawAmount > balance)
    {
      Console.WriteLine("Error: you are withdrawing too much cash.\n");
      return;
    }
      
    balance -= withdrawAmount;
    Console.WriteLine($"${withdrawAmount} have been withdrawn from your account.\n");
  }
  
  public void getBalance()
  {
    Console.WriteLine($"You have ${balance} in your account.\n");
  }
}

class Program
{
  static void Main(String[] args)
  {
    Account user = new Account();
    
    Console.WriteLine
    (
      "Welcome to my bank! There are three commands. Deposit, Withdraw, and Balance.\n" + 
      "Say 'deposit', then enter in an amount to deposit to your account.\n" +
      "Say 'withdraw', then enter in the amount to withdraw from your account.\n" +
      "Say 'balance' to check your account balance.\n"
    );
    
    while(true)
    {
      string commandLine = Console.ReadLine();
      
      if(commandLine == "Deposit" || commandLine == "deposit")
      {
        try
        {
        Console.Write("How much money would you like to deposit into your account? $");
        decimal depositAmount = Convert.ToDecimal(Console.ReadLine());
        user.deposit(depositAmount);
        }
        
        catch
        {
          Console.WriteLine("Error: Invalid input. Try again.\n");
        }
      }
      else if(commandLine == "Withdraw" || commandLine == "withdraw")
      {
        try
        {
          Console.Write("How much money would you like to withdraw into your account? $");
          decimal withdrawAmount = Convert.ToDecimal(Console.ReadLine());
          user.withdraw(withdrawAmount);
        }
        
        catch
        {
          Console.WriteLine("Error: Invalid input. Try again.\n");
        }
      }
      else if(commandLine == "Balance" || commandLine == "balance")
      {
        user.getBalance();
      }
    }
  }
}
    
