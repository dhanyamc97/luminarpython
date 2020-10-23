class Bank{

    static setBank(){
        bname="SBK";
    }
    constructor(acno,pname,balane){

        this.acno=acno;
        this.pname=pname;
        this.balane=1000;
    }

    deposit(amount){
        this.balane=amount;
        console.log("Account has been created with",this.balane,Bank.setBank)
           }

    withdraw(amount){
        if(amount>this.balane){
            console.log("Insufficient Balance");
        }
        else{
            this.balane=amount;
        }
    }

}
let obj=new Bank();
obj.deposit();
obj.withdraw();
