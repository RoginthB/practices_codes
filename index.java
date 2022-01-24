//   import BankAccount.java;
  public class Main{
    public static void main(String[] args)
    {
        BankAccount myBankAccount= new BankAccount(4141,100);
        System.out.println("YOU HAVE SUCCESSFULLY CREATED A NEW BANK ACCOUNT"+account_number);
        myBankAccount.deposit(100);
        myBankAccount.withdraw(120);
    }
}
public class BankAccount{
    private int account_number;
    private int account_balance;
   
    BankAccount myBankAccount=new BankAccount(int account_number,int account_balance)
    {
        this.account_number=account_number;
        this.account_balance=account_balance;
        System.out.println("YOUR ACCOUNT IS SUCCESSFULLY CREATED! YOUR ACCOUNT NUMBER IS:"+ account_number);
    }
    public void deposit(int addMoney)
    {
        if(addMoney <0)
        {
            System.out.println("YOU CANNOT DEPOSIT A NEGATIVE AMOUNT");
        }
        else
        {
            this.account_balance=this.account_balance+addMoney;
            System.out.println("YOUR CURRENT ACCOUNT BALANCE IS:"this.account balance);
        }
    public void withdraw(int removeMoney)
    {
        if(removeMoney>account_balance)
        {
            System.out.println("YOUR WITHDRAW AMOUNT IS GREATER THAN YOUR ACCOUNT BALANCE");
        }
        else
        {
            this.account_balance=this.account_balance-removeMoney;
            System.out.println("Rs."removeMoney + "HAS BEEN WITHDRAWNED FROM YOUR ACCOUNT NUMBER");
        }
    }
    
}