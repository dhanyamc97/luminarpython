class Maths1{

    add(){
        console.log("inside no arg method");
    }
    add(num1){
        console.log("inside one arg method");
    }
    add(num1,num2){
        console.log("inside two arg method");
    }
}

let obj=new Maths1();
//obj.add(10);
obj.add(30,20);
//obj.add();

// two argument  method will work