class Parent{
    phone(){
        console.log("parent have 0301000");

    }
}

class ChildOne extends Parent{
    n1(){
        console.log("Inside CHild One");
     }

}
class Child extends ChildOne{
}

let obj=new Child();
obj.phone();