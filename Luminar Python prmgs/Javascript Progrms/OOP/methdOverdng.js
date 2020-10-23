class Parent{

    phone(){
        console.log("parent have some nokia");
    }
}

class Child extends Parent{
    phone(){
        console.log("Have 1 phone")
    }
}

let obj=new Child()
onj.phone()