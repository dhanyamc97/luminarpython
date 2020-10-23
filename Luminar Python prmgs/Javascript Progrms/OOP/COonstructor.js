class Employee{
    constructor(id,name){
        this.id=id;
        this.name=name;
    }
    getEmp(){
        console.log(this.id);
        console.log(this.name);
    }

}

let obj = new Employee();
obj.getEmp();